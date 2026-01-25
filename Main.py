from os import system

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.twse.com.tw/zh/trading/historical/stock-day.html")
    print(page.title())
    system("pause")
    browser.close()
page.get_by_label()