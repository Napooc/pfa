from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Reservation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    guests = models.IntegerField()

    def __str__(self):
        return self.full_name
    
    
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email1 = models.EmailField()
    type_demande = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.nom

