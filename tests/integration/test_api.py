import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_validate_success():
    payload = {
        "email": "user123@gmail.com",
        "national_id": "1234567890"
    }
    response = requests.post(f"{BASE_URL}/validate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is True
    assert data["message"] == "Email and National ID are valid."

def test_fail_invalid_email_no_gmail():
    payload = {
        "email": "user123@yahoo.com",
        "national_id": "1234567890"
    }
    response = requests.post(f"{BASE_URL}/validate", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert data["valid"] is False
    assert data["errors"]["email"] == "Invalid email format."
