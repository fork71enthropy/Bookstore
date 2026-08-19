from django.contrib import admin
from .models import Carrel,Creneau,Reservation
# Register your models here.

admin.site.register(Carrel)
admin.site.register(Creneau) 
admin.site.register(Reservation)

