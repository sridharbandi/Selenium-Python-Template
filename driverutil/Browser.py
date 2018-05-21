from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager


class Browser(object):

    def __init__(self):
        self.driver = None

    def getbrowser(self, browsername):

        if browsername == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browsername == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browsername == "edge":
            self.driver = webdriver.Edge(EdgeDriverManager().install())
        elif browsername == "ie":
            self.driver = webdriver.Ie(IEDriverManager().install())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        return self.driver
