import time

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestTesterHome(object):
    def setup(self):
        options = webdriver.ChromeOptions
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)

        self.driver.implicitly_wait(10)
        self.driver.get("https://testerhome.com/")

    def test_search(self):
        self.driver.find_element_by_tag_name("input").send_keys('alibaba')
        self.driver.find_element_by_css_selector('.nav__search__addon').click()
        self.driver.find_element_by_xpath('//*[contains(., "1688")]/../../../..//*[@class="follow__control"]').click()

        # + 定位方式二：用后代先确定父亲再找最后一个儿子
        # self.driver.find_element_by_xpath('//tr[descendant::span[.="01688"]]/td[last()]').click()

        # + 定位方式三：用先辈的兄长的子孙后代来确认当前元素
        # self.driver.find_element_by_xpath('//a[@class="follow__control"][ancestor::td[preceding-sibling::td[descendant::span[text()="01688"]]]]').click()

        # + 定位方式四：在条件判断中使用.// 代替descendant::写法
        # self.driver.find_element_by_xpath('//tr[.//span[contains(.,"1688")]]/td[last()]').click()
        # self.driver.find_element_by_xpath('//tr[.//span[contains(.,"1688")]]//*[@class= "follow__control"]').click()

        self.driver.find_element_by_name('username').send_keys('13646837962')
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_class_name('modal__login__btn').click()
        time.sleep(5)

    def test_basic(self):
        self.driver.maximize_window()
        self.driver.fullscreen_window()
        self.driver.forward()
        self.driver.get_cookies()

    def test_execute_script(self):
        raw = self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(raw)

    def teardown(self):
        self.driver.quit()