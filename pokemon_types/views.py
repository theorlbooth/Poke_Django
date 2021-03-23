from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import PokemonType
from .serializers.common import PokemonTypeSerializer
from .serializers.populated import PopulatedPokemonTypeSerializer


class PokemonTypeListView(APIView):

    def get(self, _request):
        pokemon_types = PokemonType.objects.all()
        serialized_pokemon_types = PopulatedPokemonTypeSerializer(pokemon_types, many=True)
        return Response(serialized_pokemon_types.data, status=status.HTTP_200_OK)
