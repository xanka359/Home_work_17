import json

import requests
from jsonschema import validate


def test_validate_getting_single_user_method():
    response = requests.get("https://reqres.in/api/users/5")
    response_body = response.json()

    assert response.status_code == 200
    with open("schemas/single_user_info.json") as file:
        validate(response_body, schema=json.loads(file.read()))


def test_negative_getting_user_out_of_range():
    response = requests.get("https://reqres.in/api/users/70")

    assert response.status_code == 404
    assert response.json() == {}
