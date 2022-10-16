from pydantic import BaseModel
from typing import Optional, List


class PokemonLocationArea(BaseModel):
    name: str
    pokemons: List


class Location(BaseModel):
    name: str
    areas: List = []


class FindPokemon(BaseModel):
    id: Optional[int]
    name: Optional[str]
    finding_locations: List[str]
