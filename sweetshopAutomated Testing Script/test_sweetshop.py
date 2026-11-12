import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }


@pytest.fixture
def sweetshop_page(page: Page):
    page.goto("https://sweetshop.netlify.app/")
    return page


def test_homepage_loads(sweetshop_page: Page):
    assert sweetshop_page.title() == "Sweet Shop"
    assert sweetshop_page.get_by_role(
        "heading", name="Welcome to the sweet shop!"
    ).is_visible()


def test_browse_sweets_navigation(sweetshop_page: Page):
    sweetshop_page.get_by_role("link", name="Browse Sweets").click()
    assert sweetshop_page.url.endswith("/sweets")


def test_tc001_homepage_title(sweetshop_page: Page):
    """TC001 - Verify homepage title and heading"""
    expect(sweetshop_page).to_have_title("Sweet Shop")
    expect(
        sweetshop_page.get_by_role("heading", name="Welcome to the sweet shop!")
    ).to_be_visible()


def test_tc003_browse_sweets_button(sweetshop_page: Page):
    """TC003 - Verify Browse Sweets button"""
    button = sweetshop_page.locator('text="Browse Sweets"')
    expect(button).to_be_visible()
    button.click()
    expect(sweetshop_page).to_have_url("https://sweetshop.netlify.app/sweets")
    expect(
        sweetshop_page.get_by_role("heading", name="Browse sweets")
    ).to_be_visible()


def test_tc006_all_four_sweets_displayed(sweetshop_page: Page):
    """TC006 - Verify all 4 sweets are displayed"""
    sweetshop_page.goto("https://sweetshop.netlify.app/sweets")
    cards = sweetshop_page.locator(".product-card")
    expect(cards).to_have_count(4)


def test_tc007_chocolate_cups_details(sweetshop_page: Page):
    """TC007 - Verify Chocolate Cups details"""
    sweetshop_page.goto("https://sweetshop.netlify.app/sweets")
    card = sweetshop_page.locator(".product-card", has_text="Chocolate Cups")
    expect(card).to_contain_text("£1.00")
    expect(card.locator("button")).to_contain_text("Add to Basket")


def test_tc011_product_images_load(sweetshop_page: Page):
    """TC011 - Verify product images load correctly"""
    sweetshop_page.goto("https://sweetshop.netlify.app/sweets")
    images = sweetshop_page.locator("img")
    for i in range(images.count()):
        image = images.nth(i)
        expect(image).to_be_visible()
        expect(image).to_have_js_property("complete", True)
        assert image.evaluate("(element) => element.naturalWidth") > 0
