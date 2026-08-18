from django.db import models
import uuid # universally unique identifier
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import time


PREMIER_CRENEAU = time(8, 0)
DERNIER_CRENEAU = time(19, 30)

def validate_heure_lisse(value):
    if value.minute not in (0, 30) or value.second != 0 or value.microsecond != 0:
        raise ValidationError(
            f"L'heure doit être à 0 ou 30 minutes, reçu {value.strftime('%H:%M:%S')}"
        )

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

    def clean(self):
        super().clean()
        validate_heure_lisse(self.date.time())
        heure = self.date.time()
        if heure < PREMIER_CRENEAU or heure > DERNIER_CRENEAU:
            raise ValidationError(
                f"Les réservations sont possibles entre 08h00 et 19h30, reçu {self.date.strftime('%H:%M')}"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Reservation(models.Model):
    pk = models.CompositePrimaryKey("etudiant","carrel","creneau")
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    carrel = models.ForeignKey(Carrel, on_delete=models.CASCADE)
    creneau = models.ForeignKey(Creneau, on_delete=models.CASCADE)





