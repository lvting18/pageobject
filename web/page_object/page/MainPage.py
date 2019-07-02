from web.page_object.page.BasePage import BasePage
from web.page_object.page.SearchPage import SearchPage


class MainPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_name("q").send_keys(keyword)
        self.driver.find_element_by_css_selector('.nav__search__addon').click()
        return SearchPage(self.driver)