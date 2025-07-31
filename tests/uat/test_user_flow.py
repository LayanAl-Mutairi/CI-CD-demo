import requests
def test_uat_multiple_scenarios():
    # سيناريو صحيح
    payload = {"email": "validuser@gmail.com", "national_id": "1123456789"}
    response = requests.post(f"{BASE_URL}/validate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is True

    # سيناريو بريد خاطئ
    payload["email"] = "invaliduser@yahoo.com"
    response = requests.post(f"{BASE_URL}/validate", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert data["valid"] is False
    assert "email" in data["errors"]

    # سيناريو رقم هوية خاطئ
    payload = {"email": "validuser@gmail.com", "national_id": "0123456789"}
    response = requests.post(f"{BASE_URL}/validate", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert data["valid"] is False
    assert "national_id" in data["errors"]
