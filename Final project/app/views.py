from django.shortcuts import render
from .models import Contact
from .forms import LoginForm

def home(request):
    return render(request,'home.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('reservation')
        else:
             form = LoginForm()
             
             
             return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import SignUpForm

def registre(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login,html')  
    else:
        form = SignUpForm()
    return render(request, 'registre.html', {'form': form})

from django.shortcuts import render
from .models import Reservation

def reservation(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_Name')
        email = request.POST.get('Email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        guests = request.POST.get('guests')

        # Enregistrer les données dans la base de données
        reservation = Reservation(full_name=full_name, email=email, phone=phone, date=date, guests=guests)
        reservation.save()

        # Rediriger vers une page de confirmation
        return render(request, 'confirmation.html')

    return render(request, 'reservation.html')

def contact(request):
     if request.method == 'POST':
        nom = request.POST.get('nom')
        email1 = request.POST.get('email1')
        type_demande = request.POST.get('type_demande')
        message = request.POST.get('message')

        # Enregistrer les données dans la base de données
        contact = Contact(nom=nom, email1=email1, type_demande=type_demande, message=message)
        contact.save()

        # Rediriger vers une page de confirmation
        return render(request, 'confirmation.html')
     
     return render(request, 'contact.html')

def weding(request):
    return render(request,'weding.html')

def birthdays(request):
    return render(request,'birthdays.html')

def graduation(request):
    return render(request,'graduation.html')

def galery(request):
    return render(request,'galery.html')
