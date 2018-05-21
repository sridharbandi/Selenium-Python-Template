from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    SEARCHBOX = (By.ID, 'lst-ib')

    def __init__(self, driver):
        self.driver = driver

    def searchfor(self, text):
        self.driver.find_element(*self.SEARCHBOX).send_keys(text + Keys.RETURN)
