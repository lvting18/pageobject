from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from web.page_object.page.MainPage import MainPage


class TestXueqiu(object):
    def setup(self):
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")
        self.main = MainPage(self.driver)

    def test_search(self):
        self.main.search("alibaba").follow("1688")
        #todo: add assertion

    # def test_search(self):
    #     self.driver.find_element_by_name("q").send_keys('alibaba')
    #     self.driver.find_element_by_css_selector('.nav__search__addon').click()
    #     self.driver.find_element_by_xpath('//*[contains(., "1688")]/../../../..//*[@class="follow__control"]').click()
    #
    #     # + 定位方式二：用后代先确定父亲再找最后一个儿子
    #     # self.driver.find_element_by_xpath('//tr[descendant::span[.="01688"]]/td[last()]').click()
    #
    #     # + 定位方式三：用先辈的兄长的子孙后代来确认当前元素
    #     # self.driver.find_element_by_xpath('//a[@class="follow__control"][ancestor::td[preceding-sibling::td[descendant::span[text()="01688"]]]]').click()
    #
    #     # + 定位方式四：在条件判断中使用.// 代替descendant::写法
    #     # self.driver.find_element_by_xpath('//tr[.//span[contains(.,"1688")]]/td[last()]').click()
    #     # self.driver.find_element_by_xpath('//tr[.//span[contains(.,"1688")]]//*[@class= "follow__control"]').click()
    #
    #     self.driver.find_element_by_name('username').send_keys('13646837962')
    #     self.driver.find_element_by_name('password').send_keys('123456')
    #     self.driver.find_element_by_class_name('modal__login__btn').click()
        sleep(5)

    def teardown(self):
        self.driver.quit()