from django.db import models
# py manage.py makemigrations // por cada cambio que se le haga a la base de datos
# py manage.py migrate
# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return str(self.genero)
    
class Usuario(models.Model):
    rut = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False,null=False)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE,db_column='IDGenero')
    telefono = models.CharField(max_length=12)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField()

    def __str__(self):
        return (str(self.nombre)+" "+str(self.apellido_paterno)+" "+str(self.apellido_materno))