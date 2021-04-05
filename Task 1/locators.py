from selenium.webdriver.common.by import By


class Locators:
    caption_field = By.CSS_SELECTOR, '[name="sf_TextFilter"]:not([type="hidden"])'
    event_place_dropdown = By.CSS_SELECTOR, '#search-location button'
    date_from = By.CSS_SELECTOR, '[name="sf_DateFrom"]'
    date_to = By.CSS_SELECTOR, '[name="sf_DateTo"]'
    search = By.CSS_SELECTOR, '.advanced-search-block button[type="submit"]'
    buy_button = By.CSS_SELECTOR, '#eventsContainter [type="button"]'
    img = By.CSS_SELECTOR, '#eventsContainter img'
    options = By.CSS_SELECTOR, 'div.page-content'

    @staticmethod
    def arena(name):
        return By.XPATH, f'//a[text()="{name}"]'

    @staticmethod
    def event_item(name):
        return By.CSS_SELECTOR, f'[alt="{name}"]'
