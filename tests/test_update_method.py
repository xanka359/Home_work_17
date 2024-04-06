import json

import pytest
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def test_validate_getting_single_user_method():
    response = requests.put("https://reqres.in/api/users/7", data={
        "name": "Michaell",
        "job": "zion resident"
    })
    response_body = response.json()

    assert response.status_code == 200
    with open("../schemas/update_method.json") as file:
        validate(response_body, schema=json.loads(file.read()))


def test_validation_error_without_requested_field():
    response = requests.put("https://reqres.in/api/users/7", data={
        "name": "Michaell",
    })

    with pytest.raises(ValidationError):
        response_body = response.json()
        with open("../schemas/update_method.json") as file:
            validate(response_body, schema=json.loads(file.read()))
