import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_validate_success():
    url = f"{BASE_URL}/validate"
    payload = {
        "email": "user123@gmail.com",
        "national_id": "1234567890"
    }
    response = requests.post(url, json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] == True
    assert "Email and National ID are valid" in data["message"]

def test_validate_fail_invalid_email():
    url = f"{BASE_URL}/validate"
    payload = {
        "email": "user123gmail.com",
        "national_id": "1234567890"
    }
    response = requests.post(url, json=payload)
    
    assert response.status_code == 400 or response.status_code == 200
    data = response.json()
    assert data["valid"] == False

def test_validate_fail_invalid_national_id():
    url = f"{BASE_URL}/validate"
    payload = {
        "email": "user123@gmail.com",
        "national_id": "1234"
    }
    response = requests.post(url, json=payload)
    
    assert response.status_code == 400 or response.status_code == 200
    data = response.json()
    assert data["valid"] == False
