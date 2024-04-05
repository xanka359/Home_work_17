import requests


def test_delete_user():
    response_code = requests.delete("https://reqres.in/api/users/2")

    assert response_code.status_code == 204
