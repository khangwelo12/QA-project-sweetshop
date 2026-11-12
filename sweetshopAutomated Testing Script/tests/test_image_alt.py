from playwright.sync_api import Page, expect


def test_tc033_image_alt_text(page: Page):
    """TC033 - Verify alt text on product images"""
    page.goto("https://sweetshop.netlify.app/sweets")
    images = page.locator("img")

    for index in range(images.count()):
        expect(images.nth(index)).to_have_attribute("alt", r".+")
