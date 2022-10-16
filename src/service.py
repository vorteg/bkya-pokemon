from domain.pokemon_in_location import PokemonLocation
from models import PokemonData
from typing import Dict


class Pokedex:
    @staticmethod
    async def search_pokemon(pokemon: Dict):
        data = PokemonLocation(pokemon=pokemon)
        data.execute()
        return PokemonData(
            valid_location=data.valid_loc,
            no_valid_locations=data.no_valid_loc,
            best_area_pokemons=data.best_area_dic,
            areas_allocated=data.loc_areas,
            location_data_pokemons=data.location_list,
        )
