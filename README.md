# bkya-pokemon

## More details https://github.com/vorteg/bkya-pokemon/wiki

## To run App from Docker

### Create docker image

`docker build -t pokeapi .`

### Run docker

`docker run --rm -p 8000:8000 -v $(pwd)/src:/pokeapi -it pokeapi`

### Go to http://0.0.0.0:8000 or http://0.0.0.0:8000/docs using Google Chrome.

## To run App from a virtual environment

### create a virtual environment in python 3.10.5

`python -m venv .venv`

### install dependencies

`pip install -r requirements.txt`

### run server

`cd src`
`uvicorn app:app`

### Note for debug mode, from vscode only execute play in debug section, this repo contains the config files in .vscode folder.

### Go to http://localhost:8000 or http://localhost:8000/docs using Google Chrome.
