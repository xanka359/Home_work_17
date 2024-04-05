import json

import requests
from jsonschema import validate


def test_validate_create_method():
    response_code = requests.post("https://reqres.in/api/users", data={"name": "morpheus", "job": "master"})
    response_body = response_code.json()

    assert response_code.status_code == 201
    with open("schema_create.json") as file:
        validate(response_body, schema=json.loads(file.read()))


def test_options_returns_in_response_create_method():
    job = "master"
    name = "morpheus"

    response_code = requests.post("https://reqres.in/api/users", json={"name": name, "job": job})
    response_body = response_code.json()

    assert response_body["name"] == name
    assert response_body["job"] == job
