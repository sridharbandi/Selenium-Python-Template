from selenium.webdriver.common.by import By


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.linkselenium = driver.find_element(By.LINK_TEXT, "Selenium - Web Browser Automation")

    def link_selenium_present(self):
        assert self.linkselenium.is_displayed()