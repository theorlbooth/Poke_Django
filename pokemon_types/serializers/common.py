from rest_framework import serializers
from ..models import PokemonType

class PokemonTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PokemonType
        fields = '__all__'
        