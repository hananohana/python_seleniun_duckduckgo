from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class DuckDuckGoSearchPage:
    URL = 'http://duckduckgo.com'

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    RESULT_LINK = (By.XPATH, "//*[@id=\"r1-2\"]/div/h2/a[1]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def click_link(self):
        link_click = self.browser.find_element(*self.RESULT_LINK)
        link_click.click()