from django.db import models

# Create your models here.
class Cita(models.Model):
    texto= models.TextField(max_length=250)
    autor= models.TextField(max_length=100)
    fecha= models.TextField(max_length=100)
    fuente= models.TextField(max_length=100)

class Fuente(models.Model):
    Nombre= models.TextField(max_length=250)
    Tipo= models.TextField(max_length=100)