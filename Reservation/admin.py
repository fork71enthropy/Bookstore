from django.contrib import admin
from .models import Etudiant,Carrel,Creneau,Reservation
# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Carrel)
admin.site.register(Creneau) 
admin.site.register(Reservation)

