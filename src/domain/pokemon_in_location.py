from pydantic import BaseModel
from typing import Dict, Optional, List, Any
import requests

from .models import Location, PokemonLocationArea
from .validate_pokelocations import ValidatePokeLoc

REGION_URL = "https://pokeapi.co/api/v2/region/kanto/"
LOCATION_URL = "https://pokeapi.co/api/v2/location/"
AREAS_URL = "https://pokeapi.co/api/v2/location-area/"


class PokemonLocation(BaseModel):
    pokemon: Dict
    __url: str = REGION_URL
    available_locations: Optional[List[str]]
    payload: Optional[Any]
    valid_loc: Optional[List[str]]
    no_valid_loc: Optional[List[str]]
    location_list: List = []
    loc_areas: Dict = dict()
    best_location: Optional[str]
    best_area_dic: Optional[Dict]
    current_pokemons_num: Optional[int]

    @property
    def __request_available_locations(self):
        response = requests.get(self.__url)

        if response.status_code == 200:
            payload = response.json()
        results = payload.get("locations", [])
        self.available_locations = [loc["name"] for loc in results]

    @property
    def __request_available_areas(self):
        session = requests.session()
        for item in self.valid_loc:
            response = session.get(f"{LOCATION_URL}{item}")
            payload = response.json()
            results = payload.get("areas", [])
            self.loc_areas[item] = [a["name"] for a in results]

    def __get_best_location(self, number_pokemons: int, name_locattion: str):
        if not self.best_location:
            self.best_location = name_locattion
            self.current_pokemons_num = number_pokemons
            return
        if self.current_pokemons_num < number_pokemons:
            self.best_location = name_locattion
            self.current_pokemons_num = number_pokemons

    @property
    def __getting_pokemons_by_areas(self):
        session = requests.session()
        loc_list = []
        for key, val in self.loc_areas.items():
            areas_list = []
            for item in val:
                response = session.get(f"{AREAS_URL}{item}")
                payload = response.json()
                results = payload.get("pokemon_encounters", [])
                area_location = PokemonLocationArea(name=item, pokemons=results)
                areas_list.append(area_location.__dict__)
                self.__get_best_location(
                    number_pokemons=len(results), name_locattion=item
                )
            loc_list.append(Location(name=key, areas=areas_list).__dict__)
        self.location_list = loc_list

    def execute(self):
        self.__request_available_locations
        self.valid_loc, self.no_valid_loc = ValidatePokeLoc.validading_loc(
            locations_available=self.available_locations,
            finding_locations=self.pokemon["locations"],
        )
        self.__request_available_areas
        self.__getting_pokemons_by_areas
        self.best_area_dic = dict(
            name=self.best_location, pokemons_number=self.current_pokemons_num
        )
