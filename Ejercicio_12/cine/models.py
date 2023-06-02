from django.db import models
from django.urls import reverse

# Create your models here.
class genre(models.Model):
    name = models.CharField(max_length=64,help_text="Ingresar genero ")

    def __str__(self):
        return self.name

class director(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('Died',null=True,blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('director-detail', args={str(self.id)})

class pelicula(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(director, on_delete=models.CASCADE)
    summary = models.TextField(default='',max_length=100,help_text="Resumen de la pelicula")
    year = models.IntegerField()
    genero = models.ManyToManyField(genre)
    
    def __str__(self):
        return self.name
    

