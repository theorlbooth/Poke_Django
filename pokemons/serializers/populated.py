from comments.serializers.common import CommentSerializer
from ..serializers.common import PokemonSerializer
from pokemon_types.serializers.common import PokemonTypeSerializer

class PopulatedPokemonSerializer(PokemonSerializer):

    comments = CommentSerializer(many=True)
    types = PokemonTypeSerializer(many=True)
