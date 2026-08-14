# books/models.py
import uuid # universally unique identifier
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)

    def __str__(self):
        return self.title

# Now we are setting a canonical url for the model
    def get_absolute_url(self):
        return reverse("book_detail",args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(), # refers to our customer model (USER)
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review

















