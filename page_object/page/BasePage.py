import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.Client import Client


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
        return Client

    def find(self, kv) -> WebElement:
        return self.driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" % text))

    def loadSteps(self, po_path, key, **kwargs):
        file = open(po_path, 'r')
        po_data = yaml.load(file)
        po_method = po_data[key]
        po_elements = dict()
        if po_data.keys().__contains__("elements"):
            po_elements = po_data['elements']
        for step in po_method:
            step: dict
            element_platform = step
            # element_platform = dict()
            if step.keys().__contains__("element"):
                element_platform = po_elements[step['element']][Client.platform]
            else:
                pass
                # element_platform = {"by": step['by'], "locator": step['locator']}
            element: WebElement = self.driver.find_element(by=element_platform['by'], value=element_platform['locator'])
            action = str(step['action']).lower()
            if action=='click':
                element.click()
            elif action=='sendkeys':
                text = str(step['text'])
                for k,v in kwargs.items():
                    text = text.replace("$%s" %k, v)
                element.send_keys(text)
            # elif action=='text':
            #     return element.text
            else:
                print("UNKNOWN COMMAND %s" % step)