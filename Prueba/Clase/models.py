from django.db import models

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField( primary_key=True , max_length=10)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()

class proveedores(models.Model):
    cedula = models.CharField(primary_key=True, max_length=13)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    contacto = models.CharField(max_length=100)

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=10)
    fecha_elaboracion = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_caducacion = models.DecimalField(max_digits=10, decimal_place=2)
    description = models.TextField()


