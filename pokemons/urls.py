from django.urls import path
from .views import PokemonListView, PokemonDetailView, PokemonFavoriteView

urlpatterns = [
  path('', PokemonListView.as_view()),
  path('<int:pk>/', PokemonDetailView.as_view()),
  path('<int:pk>/favorite/', PokemonFavoriteView.as_view())
]
