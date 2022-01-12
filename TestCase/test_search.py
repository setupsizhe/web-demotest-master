#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from page.webpage import WebPage, sleep
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage
from selenium.webdriver.support import expected_conditions as EC



@allure.feature("测试登录模块")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_wms(self, drivers):
        """打开wms首页"""
        search = SearchPage(drivers)
        search.get_url(ini.url)

    @allure.story("拣货")
    def test_001(self,drivers):
        search = SearchPage(drivers)
        """登录系统"""
        search.inputuername("liusizhe")
        search.inputpassword("123456")
        search.click_search()
        search.click()
        search.get_url(ini.url)
        search.click_pick()
        """登录拣货"""
        search.login_station("S202")
        sleep(1)
        search.allocate_order()
        search.allocate_pod()
        var=1
        sleep(20)
        while var==1:
            search.scan_wall()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['TestCase/test_search.py'])
