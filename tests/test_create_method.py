import json
import requests

from utils import load_schema
from jsonschema import validate


def test_validate_create_method():
    response = requests.post("https://reqres.in/api/users", data={"name": "morpheus", "job": "master"})
    response_body = response.json()
    schema = load_schema("create.json")

    assert response.status_code == 201
    with open(schema) as file:
        schema = json.load(file)
        validate(response_body, schema=schema)


def test_options_returns_in_response_create_method():
    job = "master"
    name = "morpheus"

    response = requests.post("https://reqres.in/api/users", json={"name": name, "job": job})
    response_body = response.json()

    assert response_body["name"] == name
    assert response_body["job"] == job
