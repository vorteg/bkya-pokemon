from pydantic import BaseModel
from typing import List, Dict


class FindPokemon(BaseModel):
    locations: List[str]


class PokemonData(BaseModel):
    best_area_pokemons: Dict
    areas_allocated: Dict
    valid_location: List[str]
    no_valid_locations: List[str] = []
    location_data_pokemons: List
