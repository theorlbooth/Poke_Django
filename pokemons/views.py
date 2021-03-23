from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Pokemon
from .serializers.common import PokemonSerializer
from .serializers.populated import PopulatedPokemonSerializer


class PokemonListView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        pokemons = Pokemon.objects.all()
        serialized_pokemon = PopulatedPokemonSerializer(pokemons, many=True)
        return Response(serialized_pokemon.data, status=status.HTTP_200_OK)

    def post(self, request):
        pokemon_to_create = PokemonSerializer(data=request.data)
        if pokemon_to_create.is_valid():
            pokemon_to_create.save()
            return Response(pokemon_to_create.data, status=status.HTTP_201_CREATED)
        return Response(pokemon_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PokemonDetailView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_pokemon(self, pk):
        try:
            return Pokemon.objects.get(pk=pk)
        except Pokemon.DoesNotExist:
            raise NotFound()
          # raise NotFound(detail="My custom error message")

    def get(self, _request, pk):
        pokemon = self.get_pokemon(pk=pk)
        serialized_pokemon = PopulatedPokemonSerializer(pokemon)
        return Response(serialized_pokemon.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        pokemon_to_update = self.get_pokemon(pk=pk)
        updated_pokemon = PokemonSerializer(pokemon_to_update, data=request.data)
        if updated_pokemon.is_valid():
            updated_pokemon.save()
            return Response(updated_pokemon.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_pokemon.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        pokemon_to_delete = self.get_pokemon(pk=pk)
        deleted_name = pokemon_to_delete.name
        pokemon_to_delete.delete()
        return Response({ 'message': f'{deleted_name} Successfully Deleted' }, status=status.HTTP_410_GONE)
