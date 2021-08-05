from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView



# Create your views here.
class Prueba_View(TemplateView):
    template_name = "prueba.html"


class PruebaListView(ListView):
    #model = MODEL_NAME
    template_name = "home/lista.html"
    #queryset =
  ################# esta es una prueba para subir esta cagaa