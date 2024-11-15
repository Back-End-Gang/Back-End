from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Fuente(models.Model):
    TIPO_CHOICES = [
        ('libro', 'Libro'),
        ('articulo', 'Artículo'),
        ('discurso', 'Discurso'),
        # Agrega otros tipos de fuentes según sea necesario
    ]
    
    nombre = models.CharField(max_length=250, help_text="Nombre de la fuente")
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES, help_text="Tipo de fuente (ej. Libro, Artículo, Discurso)")
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Cita(models.Model):
    texto= models.TextField(max_length=250)
    autor= models.TextField(max_length=100)
    fecha= models.IntegerField(validators=[MaxValueValidator(1900),MinValueValidator(2024)])
    fuente= models.TextField(max_length=100)

