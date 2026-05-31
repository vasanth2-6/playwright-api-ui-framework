import requests

def test_products_api():
    response = requests.get(
        "https://automationexercise.com/api/productsList"
    )

    assert response.status_code == 200