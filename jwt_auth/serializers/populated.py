from ..serializers.common import UserSerializer
from pokemons.serializers.common import PokemonSerializer
from comments.serializers.common import CommentSerializer

class PopulatedUserSerializer(UserSerializer):

    created_pokemon = PokemonSerializer(many=True)
    posted_comments = CommentSerializer(many=True)
    