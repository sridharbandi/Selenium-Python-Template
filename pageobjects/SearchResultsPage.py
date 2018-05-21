from selenium.webdriver.common.by import By


class SearchResultsPage:
    LINKSELENIUM = (By.LINK_TEXT, 'Selenium - Web Browser Automation')

    def __init__(self, driver):
        self.driver = driver
        self.linkselenium = driver.find_element(By.LINK_TEXT, "")

    def link_selenium_present(self):
        assert self.driver.find_element(*self.LINKSELENIUM).is_displayed()
