import pytest

from page_object.page.App import App


class TestPrice(object):

    def test_price(self):
        # main=MainPage()
        price = App.openmain().gototab().getprice("深证成指")
        # print(price)
        # print(type(price))
        assert price > 8000

    def test_searched_is_selected(self):
        search_result = App.openmain().gotoSearch().search("alibaba")
        assert search_result.isInSelected("BABA") == False
        assert search_result.isInSelected("1688") == False

    def test_searched_user_is_followed(self):
        # search_user = App.openmain().gotoSearch().searchUser('seveniruby')
        # assert search_user == False
        App.openmain().gotoSearch().searchUser('seveniruby')
