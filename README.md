# bkya-pokemon

## To run App from Docker

### Create docker image

`docker build -t pokeapi .`
`docker run --rm -p 8000:8000 -v $(pwd)/src:/pokeapi -it pokeapi`

## To run App from a virtual environment

### create a virtual environment in python 3.10.5

`python -m venv .venv`

### install dependencies

`pip install -r requirements.txt`

### run server

`cd src`
`uvicorn app:app`

### Go to http://0.0.0.0:8000 or http://localhost:8000 using a browser.

## More details
