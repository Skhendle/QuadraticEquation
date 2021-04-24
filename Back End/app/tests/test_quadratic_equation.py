from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

# Integration tests for quadratic equation server.
url = "/quadratic_equation"

def test_quadratic_equation_pass_one():
    
    response =  client.post(
        url,
        json = {
            "a": 1,
            "b": -4,
            "c": 3
        }
    )

    assert response.status_code == 200
    assert response.json() == [3, 1]

def test_quadratic_equation_fail_two():
    
    response =  client.post(
        url,
        json = {
            "a": 1,
            "b": -4,
            "c": 5
        }
    )

    assert response.status_code == 200
    assert response.json() == "No Real Solution"

def test_quadratic_equation_fail_three():
    
    response =  client.post(
        url,
        json = {
            "a": 0,
            "b": -4,
            "c": 5
        }
    )

    assert response.status_code == 200
    assert response.json() == "Undefined Expression"