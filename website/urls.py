from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('payment/', views.payment, name='payment' ),

    path('process_payment/', views.processPayment, name='process_payment'),
   
]
