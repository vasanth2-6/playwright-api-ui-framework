def test_remove_cart(page):
    page.goto(
        "https://automationexercise.com/products",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.locator("a[href*='product_details']").first.click()

    page.locator(".cart").click()

    page.wait_for_timeout(2000)

    page.locator("text=View Cart").first.click()

    page.wait_for_timeout(3000)

    page.locator(".cart_quantity_delete").first.click()

    page.wait_for_timeout(3000)

    assert "Cart is empty" in page.content()