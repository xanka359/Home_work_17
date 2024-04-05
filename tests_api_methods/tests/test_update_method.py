import json

import pytest
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def test_validate_getting_single_user_method():
    response_code = requests.put("https://reqres.in/api/users/7", data={
        "name": "Michaell",
        "job": "zion resident"
    })
    response_body = response_code.json()

    assert response_code.status_code == 200
    with open("schema_update_method.json") as file:
        validate(response_body, schema=json.loads(file.read()))


def test_validation_error_without_requested_field():
    response_code = requests.put("https://reqres.in/api/users/7", data={
        "name": "Michaell",
    })

    with pytest.raises(ValidationError):
        response_body = response_code.json()
        with open("schema_update_method.json") as file:
            validate(response_body, schema=json.loads(file.read()))
