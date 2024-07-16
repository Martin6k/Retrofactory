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
<<<<<<< Updated upstream
    path('crud',views.crud,name='crud')
=======
    path("crud", views.crud, name = "crud"),
    path("user_add", views.user_add, name = "user_add"),
    path("user_del/<str:pk>", views.user_del, name = "user_del"),
    path("user_findEdit/<str:pk>", views.user_findEdit, name = "user_findEdit"),
    path("user_update", views.user_update, name = "user_update"),
    path("crud_genero", views.crud_genero, name = "crud_genero"),
    path("genero_add", views.genero_add, name = "genero_add"),
    path("genero_del/<str:pk>", views.genero_del, name = "genero_del"),
    path("genero_edit/<str:pk>", views.genero_edit, name = "genero_edit"),
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
    path("login", views.conectar, name = "login"),
    path("logout", views.desconectar, name = "logout"),
>>>>>>> Stashed changes
]
