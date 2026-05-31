import requests

def test_brands_api():
    response = requests.get(
        "https://automationexercise.com/api/brandsList"
    )

    assert response.status_code == 200
    assert "brands" in response.text.lower()