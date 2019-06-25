from page_object.driver.AndroidClient import AndroidClient
from page_object.page.MainPage import MainPage


class App(object):
    @classmethod
    def openmain(cls):
        AndroidClient.restart_app()
        return MainPage()