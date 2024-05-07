from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from django.contrib.auth import authenticate, login, logout
# from .models import 
# from .forms import 


# Create your views here.


def home(request):
    return render (request, 'farmerapp/home.html',{})

def register(request):
    return render (request, 'farmerapp/registerfarmer.html',{})

def addfarming(request):
    return render (request, 'farmerapp/addfarming.html',{})

def farmingdetails(request):
    return render (request, 'farmerapp/farmingdetails.html',{})

def agroproducts(request):
    return render (request, 'farmerapp/agroproducts.html',{})

def records(request):
    return render (request, 'farmerapp/records.html',{})