import json

import requests
from jsonschema import validate


def test_validate_getting_single_user_method():
    response_code = requests.get("https://reqres.in/api/users/5")
    response_body = response_code.json()

    assert response_code.status_code == 200
    with open("schema_single_user_info.json") as file:
        validate(response_body, schema=json.loads(file.read()))


def test_negative_getting_user_out_of_range():
    response_code = requests.get("https://reqres.in/api/users/70")

    assert response_code.status_code == 404
