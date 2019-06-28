from selenium.webdriver.common.by import By

from page_object.driver.Client import Client
from page_object.page.BasePage import BasePage


class TabPage(BasePage):

    def getprice(self, name):
        price_locator = (By.XPATH, "//*[contains(@resource-id,'index_name') and @text='%s']" %name +
                                   "/..//*[contains(@resource-id, 'index_price')]")
        price = self.find(price_locator).text
        return float(price)