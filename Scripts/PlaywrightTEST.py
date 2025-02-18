import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    url = 'https://www.example.com'
    browser = p.chromium.launch();
    page = browser.new_page()
    page.goto(url)
    page.screenshot(path="demo.png")
    browser.close()