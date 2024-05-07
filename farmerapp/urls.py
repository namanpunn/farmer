from django.urls import path 
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('addfarming/',views.addfarming, name='addfarming'),
    path('farmingdetails/',views.farmingdetails, name='farmingdetails'),
    path('agroproducts/',views.agroproducts, name='agroproducts'),
    path('records/',views.records, name='records'),
    
]