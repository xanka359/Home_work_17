import json

from jsonschema import validate
import pytest
import requests
from jsonschema.exceptions import ValidationError

from utils import load_schema


def test_validate_getting_single_user_method():
    response = requests.put("https://reqres.in/api/users/7", data={
        "name": "Michaell",
        "job": "zion resident"
    })
    response_body = response.json()
    schema = load_schema("update_method.json")

    assert response.status_code == 200
    with open(schema) as file:
        schema = json.load(file)
        validate(response_body, schema=schema)


def test_validation_error_without_requested_field():
    response = requests.put("https://reqres.in/api/users/7", data={
        "name": "Michaell",
    })
    schema = load_schema("update_method.json")

    with pytest.raises(ValidationError):
        response_body = response.json()
        with open(schema) as file:
            schema = json.load(file)
            validate(response_body, schema=schema)
