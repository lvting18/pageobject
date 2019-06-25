import pytest

from page_object.page.App import App


class TestPrice(object):

    def test_price(self):
        # main=MainPage()
        price = App.openmain().gototab().getprice("深证成指")
        # print(price)
        # print(type(price))
        assert price > 8000