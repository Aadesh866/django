from django.urls import path,include 
from . import views

urlpatterns =[
  path('',views.home,name='home'),
  path('room/',views.room,name='room'),
  path('about/',views.about,name='about'),
  path('menu/',views.menu,name='menu'),
  path('features/',views.features,name='features'),
  path('reservation/',views.reservation,name='reservation'),
]