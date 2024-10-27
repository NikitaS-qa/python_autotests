import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f10eba7973e67e692859390307976bba'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 7642

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_name = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()['data'][0]['trainer_name'] == 'Ник'