from constants import *
from locators import Locators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


d = webdriver.Chrome()
wait = WebDriverWait(d, TIMEOUT_s)
d.get(URL)
d.find_element(*Locators.caption_field).send_keys(QUERY + Keys.TAB)

# needs to be clicked for the arena options to become enabled
d.find_element(*Locators.event_place_dropdown).click()
d.find_element(*Locators.arena(ARENA_NAME)).click()

d.find_element(*Locators.date_from).send_keys(DATE_FROM)
d.find_element(*Locators.date_to).send_keys(DATE_TO)
d.find_element(*Locators.search).click()

# because of element hierarchy, there's no way to directly map from event name to buy button element
# so, we construct a list of img elements and look at their alt property
# the index that matches the event name is the index of the buy button of interest
img_elements = d.find_elements(*Locators.img)
buy_buttons = wait.until(EC.visibility_of_all_elements_located(Locators.buy_button))
event_index = [element.get_attribute('alt') for element in img_elements].index(EVENT_NAME)
buy_button = buy_buttons[event_index]

# the slow scrolling animation on the results pages causes our clicks to become intercepted by the cookies banner
# one workaround for this behaviour is to click using js
# another option would be to write our own EC-like class with a try/except block
# or just explicitly wait a number of seconds
d.execute_script('arguments[0].click()', buy_button)
options = wait.until(EC.visibility_of_all_elements_located(Locators.options))

print(f'Final item count: {len(options)}')
d.close()
