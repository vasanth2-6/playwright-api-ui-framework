def test_homepage(page):
    page.goto("https://automationexercise.com")
    assert page.title() != ""