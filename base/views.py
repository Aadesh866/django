from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
  return render(request,'base/home.html')


def room(request):
  return render(request,'base/room.html')

def about(request):
  return render(request,'base/about.html')

def menu(request):
  return render(request,'base/menu.html')

def features(request):
  return render(request,'base/features.html')

def reservation(request):
  return render(request,'base/reservation.html')