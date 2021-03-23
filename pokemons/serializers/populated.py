from comments.serializers.common import CommentSerializer
from pokemon_types.serializers.common import PokemonTypeSerializer
from ..serializers.common import PokemonSerializer


class PopulatedPokemonSerializer(PokemonSerializer):

    comments = CommentSerializer(many=True)
    types = PokemonTypeSerializer(many=True)
