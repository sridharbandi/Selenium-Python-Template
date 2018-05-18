import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://www.google.com")
        self.driver.quit()

