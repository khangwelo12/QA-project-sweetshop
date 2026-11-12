from playwright.sync_api import Page, expect


def test_tc026_mobile_view(page: Page):
    """TC026 - Verify sweets page on mobile (375px)"""
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("https://sweetshop.netlify.app/sweets")

    expect(page.locator(".card").first).to_be_visible()
    assert page.evaluate(
        "() => document.documentElement.scrollWidth <= "
        "document.documentElement.clientWidth"
    ), "Page has horizontal overflow at mobile width"
