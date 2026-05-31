import requests

def test_search_product_api():
    payload = {
        "search_product": "top"
    }

    response = requests.post(
        "https://automationexercise.com/api/searchProduct",
        data=payload
    )

    assert response.status_code == 200