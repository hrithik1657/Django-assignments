from django.contrib import admin

# Register your models here.
from imdb_1.models import Actor, Movie, Rating, Director, MovieCast

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(MovieCast)
admin.site.register(Movie)
admin.site.register(Rating)
