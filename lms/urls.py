from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    
    path('',Book),
    path('create/',PostBook),
    path('update/<int:id>/',UpdateBook),
    path('deleteboook/<int:id>/',DeleteBook),
]