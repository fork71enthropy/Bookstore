from django.db import models
import uuid # universally unique identifier
from django.contrib.auth.models import AbstractUser



class Etudiant(AbstractUser):
    email = models.EmailField(primary_key=True, max_length=255)
    hours = models.IntegerField(max_value=20, default=20) # pas plus de 20 heures
    # id == email    

class Carrel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    numero = models.IntegerField(max_value=444) # Je crois que 444 c'est le max
    etage = models.IntegerField(max_value=4)
    nb_places = models.IntegerField(max_value=2)

class Creneau(models.Model):
    pk = models.CompositePrimaryKey("date","duration")
    duration = models.IntegerField(max_value=12)
    date = models.DateTimeField()

class Reservation(models.Model):
    pk = models.CompositePrimaryKey("etudiant","carrel","creneau")
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    carrel = models.ForeignKey(Carrel, on_delete=models.CASCADE)
    creneau = models.ForeignKey(Creneau, on_delete=models.CASCADE)






    """id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False

    )"""