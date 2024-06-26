from django.shortcuts import render
from .models import Genero, Usuario, Producto, Categoria

# Create your views here.
def index(request):
    context={}
    return render(request,'pages/index.html', context)

def juegos(request):
    context={}
    return render(request,'pages/juegos.html',context)

def accesorios(request):
    context={}
    return render(request,'pages/accesorios.html',context)

def contacto(request):
    context={}
    return render(request,'pages/contacto.html',context)

def carrito(request):
    context={}
    return render(request,'pages/carrito.html',context)

def sesion(request):
    context={}
    return render(request,'pages/sesion.html',context)

def crearsesion(request):
    context={}
    return render(request,'pages/crearsesion.html',context)

def crearsesion2(request):
    context={
    }
    return render(request,'pages/crearsesion2.html',context)