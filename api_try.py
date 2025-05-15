import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Alles accepteren").click()
    page.get_by_role("combobox", name="Zoek").click()
    page.get_by_role("combobox", name="Zoek").fill("playw")
    page.get_by_role("combobox", name="Zoek").press("ArrowDown")
    page.locator("iframe[name=\"a-k6jq13ojsa6p\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    page.locator("div:nth-child(2) > div").first.click()
    page.locator("iframe[name=\"a-k6jq13ojsa6p\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    page.locator("div:nth-child(2) > div").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)