from ..serializers.common import PokemonTypeSerializer
from pokemons.serializers.common import PokemonSerializer

class PopulatedPokemonTypeSerializer(PokemonTypeSerializer):

    pokemons = PokemonSerializer(many=True)
