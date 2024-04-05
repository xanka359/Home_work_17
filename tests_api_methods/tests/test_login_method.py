import json

import requests
from jsonschema import validate

url = "https://reqres.in/api/login"
payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}


def test_validate_login_method():
    response_code = requests.post(url=url, data=payload)
    response_body = response_code.json()

    assert response_code.status_code == 200
    with open("schema_login.json") as file:
        validate(response_body, schema=json.loads(file.read()))


def test_unsuccessful_login_without_password():
    response_code = requests.post(url=url, data={"email": "peter@klaven"})
    response_body = response_code.json()
    expected_response = {"error": "Missing password"}

    assert response_code.status_code == 400
    validate(response_body, schema=expected_response)


def test_unsuccessful_login_without_login():
    response_code = requests.post(url=url, data={"password": "cityslicka"})
    response_body = response_code.json()
    expected_response = {"error": "Missing email or username"}

    assert response_code.status_code == 400
    validate(response_body, schema=expected_response)
