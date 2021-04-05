from locators import Locators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


TIMEOUT_s = 3
URL = 'https://www.tiketa.lt/EN/search'
ARENA_NAME = 'Avia Solutions Group arena'
EVENT_NAME = 'CIRQUE DU SOLEIL - CORTEO'
QUERY = 'Corteo'


d = webdriver.Chrome()
wait = WebDriverWait(d, TIMEOUT_s)
d.get(URL)
d.find_element(*Locators.caption_field).send_keys(QUERY + Keys.TAB)
d.find_element(*Locators.event_place_dropdown).click()
d.find_element(*Locators.arena(ARENA_NAME)).click()
d.find_element(*Locators.date_from).send_keys('2022-01-01')
d.find_element(*Locators.date_to).send_keys('2022-03-31')
d.find_element(*Locators.search).click()
event_item = wait.until(EC.element_to_be_clickable(Locators.event_item(EVENT_NAME)))
buy_buttons = d.find_elements(*Locators.buy_button)
img_elements = d.find_elements(*Locators.img)
buy_button = buy_buttons[[element.get_attribute('alt') for element in img_elements].index(EVENT_NAME)]
d.execute_script('arguments[0].click()', buy_button)
options = wait.until(EC.visibility_of_all_elements_located(Locators.options))
print(f'Final item count: {len(options)}')
d.close()
