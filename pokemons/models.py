from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=30, unique=True)
    number = models.PositiveIntegerField(unique=True)
    is_starter = models.BooleanField(default=False)
    generation = models.PositiveIntegerField()
    pokedex_entry = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    types = models.ManyToManyField(
        'pokemon_types.PokemonType',
        related_name='pokemons'
    )
    owner = models.ForeignKey(
      'jwt_auth.User',
      related_name='created_pokemon',
      on_delete=models.CASCADE
    )
    favorited_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='favorited_pokemon',
        blank=True
    )

    def __str__(self):
        return f"{self.number} - {self.name}"
