from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.login, name="login"),
    path('registre/', views.registre, name='registre'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('weding', views.weding, name='weding'),
    path('birthdays', views.birthdays, name='birthdays'),
    path('graduation', views.graduation, name='graduation'),
     path('galery', views.galery, name='galery'),
     
]