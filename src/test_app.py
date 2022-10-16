from fastapi.testclient import TestClient
import os
import json

from app import app

cwd = os.getcwd()
print(cwd)
client = TestClient(app)
path_file_empty = "src/request_body_tests/request_body_empty.json"
path_file_challenge = "src/request_body_tests/request_body_challenge.json"


def test_main():
    """Test case: When the body request has been the correct"""
    path = f"{cwd}/{path_file_challenge}"
    with open(path, "rb") as file:
        json_file = json.load(file)
    response = client.post("/pokemon-in-location", json=json_file)
    assert response.status_code == 200


def test_main_fail():
    """Test case: Json Body Empty"""
    path = f"{cwd}/{path_file_empty}"
    with open(path, "rb") as file:
        json_file = json.load(file)
    response = client.post("/pokemon-in-location", json=json_file)
    assert response.status_code == 422
