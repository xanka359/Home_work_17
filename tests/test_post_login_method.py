import json

import requests
from jsonschema import validate

url = "https://reqres.in/api/login"
payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}


def test_validate_login_method():
    response = requests.post(url=url, data=payload)
    response_body = response.json()

    assert response.status_code == 200
    with open("../schemas/login.json") as file:
        validate(response_body, schema=json.loads(file.read()))


def test_unsuccessful_login_without_password():
    response = requests.post(url=url, data={"email": "peter@klaven"})
    response_body = response.json()
    expected_response = {"error": "Missing password"}

    assert response.status_code == 400
    validate(response_body, schema=expected_response)


def test_unsuccessful_login_without_email():
    response = requests.post(url=url, data={"password": "cityslicka"})
    response_body = response.json()
    expected_response = {"error": "Missing email or username"}

    assert response.status_code == 400
    validate(response_body, schema=expected_response)
