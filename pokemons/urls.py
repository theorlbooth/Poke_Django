from django.urls import path
from .views import PokemonListView, PokemonDetailView

urlpatterns = [
  path('', PokemonListView.as_view()),
  path('<int:pk>/', PokemonDetailView.as_view())
]
