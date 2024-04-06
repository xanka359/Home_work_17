import requests
import jsonschema

from utils import load_schema


def test_validate_getting_single_user_method():
    response = requests.get("https://reqres.in/api/users/5")
    response_body = response.json()
    schema = load_schema("../schemas/single_user_info.json")

    assert response.status_code == 200
    jsonschema.validate(response_body, schema)


def test_negative_getting_user_out_of_range():
    response = requests.get("https://reqres.in/api/users/70")

    assert response.status_code == 404
    assert response.json() == {}
