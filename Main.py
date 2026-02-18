from os import system

from playwright.sync_api import sync_playwright
stock_year = input("請輸入查詢年分 (例如 2026): ")
if not stock_year.strip():
    print('錯誤，日期不可為空!')
    exit()

stock_month = input("請輸入查詢月分 (例如 2): ")
if not stock_month.strip():
    print('錯誤，日期不可為空!')
    exit()

stock_id = input("請輸入股票代碼 (例如 2330): ")
if not stock_id.strip():
    print('錯誤，股票代碼不可為空!')
    exit()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.twse.com.tw/zh/trading/historical/stock-day.html")
    print(page.title())
    page.select_option('#label0', value=stock_year)
    page.select_option('select[name="mm"]', value=stock_month)
    page.get_by_label("股票代碼").fill(stock_id)
    page.click('button.search')
    page.wait_for_selector('table.main-list')
    rows = page.query_selector_all('table.main-list tr')
    system("pause")
    browser.close()
