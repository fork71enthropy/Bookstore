from django.db import models
import uuid # universally unique identifier
#from django.contrib.auth.models import AbstractUser ; un étudiant c'est juste une adresse mail et un quota d'heures
from django.core.exceptions import ValidationError
from datetime import time
from django.core.validators import MaxValueValidator, MinValueValidator


PREMIER_CRENEAU = time(8, 0)
DERNIER_CRENEAU = time(19, 00)

def validate_heure_lisse(value):
    if value.minute not in (0, 30) or value.second != 0 or value.microsecond != 0:
        raise ValidationError(
            f"L'heure doit être à 0 ou 30 minutes, reçu {value.strftime('%H:%M:%S')}"
        )

class Etudiant(models.Model):
    email = models.EmailField(primary_key=True, max_length=255)
    hours = models.IntegerField(
    default=20,
    validators=[MaxValueValidator(20), MinValueValidator(0)]
)
    # id == email    

class Carrel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    numero = models.IntegerField(validators=[MaxValueValidator(444), MinValueValidator(2)]) # Je crois que 444 c'est le max
    etage = models.IntegerField(    validators=[MaxValueValidator(4), MinValueValidator(0)])
    nb_places = models.IntegerField(validators=[MaxValueValidator(2), MinValueValidator(0)])

class Creneau(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    duration = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    date = models.DateTimeField()

    class Meta:
        unique_together = ("date", "duration")

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    carrel = models.ForeignKey(Carrel, on_delete=models.CASCADE)
    creneau = models.ForeignKey(Creneau, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("etudiant", "carrel", "creneau")













