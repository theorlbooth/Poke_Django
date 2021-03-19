from comments.serializers.common import CommentSerializer
from ..serializers.common import PokemonSerializer

class PopulatedPokemonSerializer(PokemonSerializer):

    comments = CommentSerializer(many=True)
