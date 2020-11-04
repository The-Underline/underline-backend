import time
from fastapi.testclient import TestClient
from app import app
import pytest
import logging

client = TestClient(app)

# methods for testing get user 
def get_user_registration_form():
    user_data = {
        "first_name": "Testing_first",
        "last_name": "Testing_last",
        "email": "test@mail.com"
    }
    return user_data

def check_get_user_response_valid(response):
    valid = True
    valid = valid and response.status_code == 201
    valid = valid and "user_id" in response.json()
    return valid


# used to test "/users/find"
class TestGetUser:
    def test_get_user_success(self):
        # get fake user data to test
        user_data = get_user_registration_form()
        # send request to test client
        response = client.get("/users/find", json=user_data)
        breakpoint()
        # check that response is good
        assert check_get_user_response_valid(response)

    def test_get_user_empty_data_failure(self):
        # send request to test client
        response = client.post("/users/register", json={})
        # check that response is good
        assert not check_user_register_response_valid(response)


