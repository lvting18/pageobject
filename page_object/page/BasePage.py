from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver = self.getClient().driver
        # self.driver = self.getDriver()

    # @classmethod
    # def getDriver(cls):
    #     cls.driver = AndroidClient.driver
    #     return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" % text))