import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_complete_user_flow():
    # اختبار يدمج خطوات متعددة ممكنة في التطبيق
    payload = {
        "email": "test.user@example.com",
        "national_id": "1234567890"
    }
    response = requests.post(f"{BASE_URL}/validate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data.get("valid") == True
    assert "valid" in data.get("message").lower()
