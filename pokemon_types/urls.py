from django.urls import path
from .views import PokemonTypeListView

urlpatterns = [
  path('', PokemonTypeListView.as_view())
]
