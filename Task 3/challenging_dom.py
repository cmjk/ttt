from selenium import webdriver
from time import sleep

URL = 'http://the-internet.herokuapp.com/challenging_dom'
GREEN_BUTTON_LOCATOR = 'a.button.success'


def highlight_element(element, duration):
    script = "arguments[0].setAttribute('style', arguments[1]);"
    driver = element._parent
    original_style = element.get_attribute('style')
    driver.execute_script(script, element, 'border: 3px solid red;')
    sleep(duration)
    driver.execute_script(script, element, original_style)


def highlight_row_of_column(driver: webdriver.Chrome, column_name: str, row_index: int, duration_s: int = 2) -> None:
    header = driver.find_elements_by_css_selector('thead th')
    column_index = [item.text for item in header].index(column_name)
    cell_locator = f'tr:nth-child({row_index}) td:nth-child({column_index + 1})'
    cell_element = d.find_element_by_css_selector(cell_locator)
    highlight_element(cell_element, duration_s)


def highlight_row_item_from_text(driver: webdriver.Chrome, text_value: str, button: str = '', duration_s: int = 2) -> None:
    locator = f'//td[text() = "{text_value}"]'
    if button:
        locator += f'/..//a[@href="#{button}"]'
    element = driver.find_element_by_xpath(locator)
    highlight_element(element, duration_s)


d = webdriver.Chrome()
d.get(URL)

highlight_row_of_column(d, 'Diceret', 3)
highlight_row_item_from_text(d, 'Apeirian7', button='delete')
highlight_row_item_from_text(d, 'Apeirian2', button='edit')
highlight_row_item_from_text(d, 'Definiebas7')
highlight_row_item_from_text(d, 'Iuvaret7')
d.find_element_by_css_selector(GREEN_BUTTON_LOCATOR).click()
d.close()
