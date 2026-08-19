from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CustomUser(AbstractUser):
    hours = models.IntegerField(
    default=20,
    validators=[MaxValueValidator(20), MinValueValidator(0)]
)














