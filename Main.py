from os import system

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.twse.com.tw/zh/trading/historical/stock-day.html")
    print(page.title())
    page.get_by_label("股票代碼").fill("2330")
    page.click('button.search')
    page.wait_for_selector('table.main-list')
    rows = page.query_selector_all('table.main-list tr')
    system("pause")
    browser.close()
