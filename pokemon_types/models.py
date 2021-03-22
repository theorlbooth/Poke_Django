from django.db import models

class PokemonType(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name}'
