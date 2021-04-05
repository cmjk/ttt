from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

TIMEOUT_s = 3


URL = 'https://www.tiketa.lt/EN/search'
caption_field_locator = '[name="sf_TextFilter"]:not([type="hidden"])'
event_place_dropdown_locator = '#search-location button'
arena_locator = '//a[text()="Avia Solutions Group arena"]'
date_from_locator = '[name="sf_DateFrom"]'
date_to_locator = '[name="sf_DateTo"]'
search_locator = '.advanced-search-block button[type="submit"]'
event_item_locator = '[alt="CIRQUE DU SOLEIL - CORTEO"]'
buy_button_locator = '#eventsContainter [type="button"]'
img_element_locator = '#eventsContainter img'
items_locator = 'div.page-content'

d = webdriver.Chrome()
wait = WebDriverWait(d, TIMEOUT_s)
d.get(URL)
d.find_element_by_css_selector(caption_field_locator).send_keys('Corteo' + Keys.TAB)
d.find_element_by_css_selector(event_place_dropdown_locator).click()
d.find_element_by_xpath(arena_locator).click()
d.find_element_by_css_selector(date_from_locator).send_keys('2022-01-01')
d.find_element_by_css_selector(date_to_locator).send_keys('2022-03-31')
d.find_element_by_css_selector(search_locator).click()
event_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, event_item_locator)))
buy_buttons = d.find_elements_by_css_selector(buy_button_locator)
img_elements = d.find_elements_by_css_selector(img_element_locator)
buy_button = buy_buttons[[element.get_attribute('alt') for element in img_elements].index("CIRQUE DU SOLEIL - CORTEO")]
d.execute_script('arguments[0].click()', buy_button)
items = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, items_locator)))
print(f'Final item count: {len(items)}')
d.close()
