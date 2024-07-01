from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('juegos',views.juegos,name='juegos'),
    path('accesorios',views.accesorios,name='accesorios'),
    path('contacto',views.contacto,name='contacto'),
    path('carrito',views.carrito,name='carrito'),
    path('sesion',views.sesion,name='sesion'),
    path('crearsesion',views.crearsesion,name='crearsesion'),
    path('crearsesion2',views.crearsesion2,name='crearsesion2'),
    path("crud", views.crud, name = "crud"),
    path("user_add", views.user_add, name = "user_add"),
    path("user_del/<str:pk>", views.user_del, name = "user_del"),

]
