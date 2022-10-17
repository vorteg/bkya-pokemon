from fastapi import FastAPI, HTTPException, status
from models import FindPokemon, PokemonData
from service import Pokedex

app = FastAPI(
    title="Pokemon Location Areas in Kanto Region",
)


@app.get("/")
def welcome():
    """A Welcome Message."""
    return {
        "msg": "Please go to url /docs or /redoc for more details about endpoints use"
    }


@app.post("/pokemon-in-location", response_model=PokemonData)
async def main(pokemon: FindPokemon):
    """This endpoint is to locate pokemons and verify if the locations exist in kanto region."""
    if pokemon.locations:
        return await Pokedex.search_pokemon(pokemon.__dict__)
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail="Request body is incorrect. Please insert into the body request a valid location list into Kanto Region.",
    )
