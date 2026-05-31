def test_product_details(page):
    page.goto(
        "https://automationexercise.com/products",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.locator("a[href*='product_details']").first.click()

    assert "product_details" in page.url