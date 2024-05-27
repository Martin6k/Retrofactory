from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('juegos',views.juegos,name='juegos'),
    path('accesorios',views.accesorios,name='accesorios'),
    path('contacto',views.contacto,name='contacto'),
    path('carrito',views.carrito,name='carrito'),
    path('sesion',views.sesion,name='sesion'),
    path('crearsesion',views.crearsesion,name='crearsesion')
]
