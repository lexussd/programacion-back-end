from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Crear nuestra primera vista en python
#Nos mostrara un hola mundo

def display(request):
    return HttpResponse("<h1>Hola Mundo Nicolas<h1/>")

#segunda vista en nuestra APP
def displayDatetime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora actual: <b/>" + str(dt)
    return HttpResponse(s)

def formulario(request):
    return HttpResponse("<button>Enviar</button>")