import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def basket_page(page: Page):
    page.goto("https://sweetshop.netlify.app/sweets")
    return page


def test_tc014_add_one_item(basket_page: Page):
    """TC014 - Add one item to basket"""
    basket_page.locator(".card").first.get_by_text(
        "Add to Basket", exact=True
    ).click()

    expect(basket_page.locator('a[href="/basket"] .badge')).to_have_text("1")


def test_tc016_add_all_four_sweets(basket_page: Page):
    """TC016 - Add the first four different sweets to basket"""
    cards = basket_page.locator(".card")
    for index in range(4):
        cards.nth(index).get_by_text("Add to Basket", exact=True).click()

    expect(basket_page.locator('a[href="/basket"] .badge')).to_have_text("4")
