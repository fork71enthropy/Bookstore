from django.shortcuts import render
from django.views.generic import ListView
from .models import Carel
# Create your views here.
class CarelListView(ListView):
    model = Carel
    context_object_name = "carels_dispos"
    template_name = "reservations/carels.html"

