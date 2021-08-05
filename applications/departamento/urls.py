
from django.contrib import admin
from django.urls import path

def DesdeApps (self):
    print ('**********-------------esta ejecutando desde app departamento')

urlpatterns = [
    
    path('departamento/', DesdeApps),
]
