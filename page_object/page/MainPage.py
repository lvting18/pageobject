from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.SearchPage import SearchPage
from page_object.page.TabPage import TabPage


class MainPage(BasePage):
    _profile_button = (By.ID, "user_profile_icon")
    def gototab(self):
        # tab_locator = (By.XPATH, "//*[@text='行情']")
        tab = "行情"
        self.findByText(tab)
        self.findByText(tab).click()
        # self.driver.find_element(By.XPATH, "//*[@text='行情']").click()
        return TabPage()

    def gotoSearch(self):
        search_box = (By.ID, "home_search")
        self.find(search_box).click()
        return SearchPage()

    def gotoProfile(self):
        self.find(MainPage._profile_button).click()
        return ProfilePage()
