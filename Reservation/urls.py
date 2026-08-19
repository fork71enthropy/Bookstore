from django.urls import path
from .views import CarelListView


urlpatterns = [
    path("",CarelListView.as_view(),name="carels_dispos"),

]


#carels_dispos











































