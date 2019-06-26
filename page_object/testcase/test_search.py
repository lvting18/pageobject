import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage


class TestPrice(object):

    @classmethod
    def setup_class(cls):
        cls.mainPage = App.openmain()

    def setup_method(self):
        self.mainPage: MainPage = TestPrice.mainPage
        self.SearchPage = self.mainPage.gotoSearch()

    def teardown_method(self):
        self.SearchPage.cancelSearch()

    def test_searched_stock_is_selected(self):
        search_result = self.SearchPage.search("alibaba")
        assert search_result.isInSelected("BABA") == False
        assert search_result.isInSelected("1688") == False

    @pytest.mark.parametrize('username, result',
                             [('seveniruby', True),
                              ('lvting', False)])
    def test_searched_user_is_followed(self, username, result):
        assert self.SearchPage.searchUser(username) == result
