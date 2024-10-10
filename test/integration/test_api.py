import requests

def test_get_temperature_api():
    response = requests.get("http://127.0.0.1:5000/temperature")
    assert response.status_code == 200
    assert "temperature" in response.json()
