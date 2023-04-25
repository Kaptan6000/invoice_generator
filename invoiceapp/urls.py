from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('makeinvoice/',views.makeinvoice),
    path('generateinvoice/0/', views.GenerateInvoice, name = 'generateinvoice'),
    # path('generate/',views.generate)
]