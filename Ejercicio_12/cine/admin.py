from django.contrib import admin
from .models import director, pelicula, genre

# Register your models here.
admin.site.register(director)
admin.site.register(pelicula)
admin.site.register(genre)