from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return str(self.genero)
    
class Usuario(models.Model):
    rut = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField(blank=False,null=False)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE,db_column='idGenero')
    telefono = models.CharField(max_length=12)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    contraseña = models.CharField(max_length=15, null=False, blank=False,default='null')

    def __str__(self):
        return (str(self.nombre))
    
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=10,blank=True, null=False)

    def __str__(self):
        return str(self.categoria)

class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')
    descripcion = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return str(self.descripcion)
