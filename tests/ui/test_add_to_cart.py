def test_add_to_cart(page):
    page.goto(
        "https://automationexercise.com/products",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.locator("a[href*='product_details']").first.click()

    page.locator(".cart").click()

    page.wait_for_timeout(3000)

    assert page.locator("text=View Cart").first.is_visible()