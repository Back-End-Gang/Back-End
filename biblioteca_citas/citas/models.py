from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Cita(models.Model):
    texto= models.TextField(max_length=250)
    autor= models.TextField(max_length=100)
    fecha= models.IntegerField(validators=[MaxValueValidator(1900),MinValueValidator(2024)])
    fuente= models.TextField(max_length=100)

class Fuente(models.Model):
    Nombre= models.TextField(max_length=250)
    Tipo= models.TextField(max_length=100)