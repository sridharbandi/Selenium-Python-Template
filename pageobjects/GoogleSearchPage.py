from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.searchbox = driver.find_element(By.ID, "lst-ib")

    def searchfor(self, text):
        self.searchbox.send_keys(text + Keys.RETURN)
