from comments.serializers.populated import PopulatedCommentSerializer
from ..serializers.common import PokemonSerializer
from pokemon_types.serializers.common import PokemonTypeSerializer
from jwt_auth.serializers.common import NestedUserSerializer

class PopulatedPokemonSerializer(PokemonSerializer):

    comments = PopulatedCommentSerializer(many=True)
    types = PokemonTypeSerializer(many=True)
    owner = NestedUserSerializer()
