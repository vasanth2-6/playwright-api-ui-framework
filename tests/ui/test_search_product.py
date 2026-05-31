def test_search_product(page):
    page.goto("https://automationexercise.com/products")

    page.fill("#search_product", "Blue Top")
    page.click("#submit_search")

    assert page.locator(".productinfo p").first.is_visible()