from playwright.sync_api import Page
import pytest


def test_title(page: Page):
    page.goto('https://www.saucedemo.com/')
    assert page.title() =="Swag Labs"

def test_inventory_test(page: Page):
    page.goto('https://www.saucedemo.com/inventory.html')
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."

