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

def crud(request):
    usuarios = Usuario.object.all()
    context = {
        "usuarios":usuarios,
    }
    return render(request, "pages/crud.html", context)

def user_add(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {
            "generos":generos,
        }
        return render(request,"pages/user_add.html", context)
    else:
        correo = request.POST["correo"]
        nombre = request.POST["nombre"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        password = request.POST["password"]
        activo = True

        objGenero = Genero.objects.get(id_genero = genero)
        obj = Usuario.objects.create(
            email =  correo,
            nombre = nombre,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            contraseña = password,
            activo = activo,
        )
        obj.save()
        context = {
            "mensaje": "Registro exitoso",
        }
        return render(request, "pages/user_add.html", context)

def user_def(request, pk):
    try:
        usuario = Usuario.objects.get(email=pk)
        usuario.delete()
        usuarios = Usuario.objects.all()
        context = {
            "mensaje":"Eliminado con exito",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)
    except:
        usuario = usuario.objects.all()
        context = {
            "mensaje": "Error, correo no encontrado...",
            "usuarios": usuarios,
        }
