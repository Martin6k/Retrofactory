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

def user_del(request, pk):
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
        return render(request, "pages/crud.html", context)

def user_findEdit (request,pk):
    if pk != "":
        usuario = Usuario.objects.get(email=pk)
        generos = Genero.objects.all()
        context = {
            "generos":generos,
            "usuario":usuario,
        }
        return render(request, "pages/user_update.html", context)
    else:
        usuarios = Usuario.ojbects.all()
        context = {
            "mensaje":"Error, email no encontrado",
            "usuarios":usuario
        }
        return render(request, "pages/crud.html", context)

def user_update(request):
    if request.method=="POST":

        correo = request.POST["correo"]
        nombre = request.POST["nombre"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        password = request.POST["password"]
        activo = True     

        objGenero = Genero.objects.get(id_genero = genero)

        obj = Usuario(

            email =  correo,
            nombre = nombre,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            contraseña = password,
            activo = activo,

        )
        obj.save()

        generos = Genero.objects.all()
        context = {
            "mensaje": "Modificado con exito",
            "generos":generos,
            "usuario":obj,
        }
        return render(request, "pages/user_update.html", context)

def crud_genero(request):
    generos = Genero.objects.all()
    context = {
        "generos": generos,
    }
    return render(request, "pages/crud_genero.html", context)

def genero_add(request):
    formGenero = GeneroForm()
    if request.method == "POST":
        nuevo = GeneroForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context = {
                "mensaje": "Agregado con exito",
                "form":formGenero,
            }
            return render(request, "pages/genero_add.html", context)
        
    else:
        context = {
            "form":formGenero,
        }
        return render(request, "pages/genero:_add.html", context)

def genero_del(request, pk):
    try:
        genero = Genero.objects.get(id_genero = pk)
        genero.delete()

        generos = Genero.objects.all()
        context = {
            "mensaje":"Eliminado con exito",
            "generos":generos
        }
        return render(request, "pages/crud_genero.html", context)
    
    except: 
        generos = Genero.objects.all()
        context = {
            "mensaje":"Error, Genero no encontrado",
            "generos":generos
        }
        return render(request, "pages/crud_genero.html", context)

def genero_edit(request, pk):
    if pk!="":
        genero = Genero.objects.get(id_genero = pk)

        if request.method == "POST":
            nuevo = GeneroForm(request.POST,instance = genero)
            if nuevo.is_valid():
                nuevo.save()

                context = {
                    "mensaje":"Modificacion exitosa",
                    "form":nuevo
                }
                return render(request, "pages/genero_edit.html", context)
        else:
          form = GeneroForm(instance = genero)

          context = {
              "form":form,
          }
          return render(request, "pages/genero_edit.html", context)
    else: 
        generos = Genero.objects.all()
        context = {
            "mensaje":"Error, genero no encontrado...",
            "generos":generos,
        }
        return render(request, "pages/crud_genero.html", context)
    



        