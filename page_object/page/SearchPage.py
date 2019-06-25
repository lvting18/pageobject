from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    input_box = (By.ID, 'search_input_text')

    def search(self, key):
        self.find(self.input_box).send_keys(key)
        return self

    def isInSelected(self, key):
        add_button = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and contains(@text, %s)]" % key +
                                 "/../../..//*[contains(@resource-id, 'follow')]")
        id = self.find(add_button).get_attribute("resourceId")
        print(id)
        return "followed_btn" in id

    def searchUser(self, key):
        self.search(key)
        self.findByText("用户").click()
        follow_button = (By.XPATH, "//*[@text='"+key+"']/../..//*[contains(@resource-id, 'follow_btn')]")
        status = self.find(follow_button).text
        print(status)
        # return "已关注" in status
