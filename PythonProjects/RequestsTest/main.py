import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f10eba7973e67e692859390307976bba'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

BODY_create = {
    "name": "ROMA",
    "photo_id": 11
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_create)
print(response_create.text)

POKEMON_ID = response_create.json()['id']

BODY_new_name = {
    "pokemon_id": POKEMON_ID,
    "name": "REBUS",
    "photo_id": 23
}

BODY_ADD_POKEBALL = {
    "pokemon_id": POKEMON_ID
}

response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_new_name)
print(response_new_name.text)

response_new_name = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_ADD_POKEBALL)
print(response_new_name.text)