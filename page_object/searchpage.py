#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from selenium.webdriver.support import expected_conditions as EC

search = Element('search')

class SearchPage(WebPage):
    """搜索类"""
    def inputuername(self,content):
        "登录"
        self.input_text(search["账号"],txt=content)
        sleep()
    def inputpassword(self,content):
        self.input_text(search["密码"],txt=content)
        sleep()
        # self.is_click(search["登录"])
    def input_search(self, content):
        """输入搜索"""
        self.input_text(search['搜索框'], txt=content)
        sleep()

    def click_search(self):
        """点击搜索"""
        self.is_click(search['登录'])
    def click(self):
        self.is_click(search['选择仓库'])
    def click_pick(self):
        self.is_click(search['拣货按钮'])
    def login_station(self,content):
        self.auto_enter(search['登录拣货工作站'], txt=content)
    def enter(self,content):
        self.auto_enter()
    def allocate_order(self):
        self.is_click(search['分配容器'])
    def allocate_pod(self):
        self.is_click(search['分配订单'])
    # def click_pod(self):
    #     self.is_click(search['确认货架'])
    def refresh_pod(self):
        self.is_click(search['刷新货架'])
    def finish_picking(self):
        self.is_click(search['退出拣货'])
    def sure_finish(self):
        self.is_click(search['确认退出拣货'])
    def scan_wall(self):
        # print(len(self.text1()))
        if len(self.text1()) != 0:
            for code1 in self.text1():
                self.auto_enter(search['输入拣货分播墙格子'], txt=code1)
                sleep(3)
            for code2 in self.text2():
                self.auto_enter(search['输入满箱分播墙格子'],txt=code2)
                sleep(3)
            self.refresh_pod()
        else:
            self.refresh_pod()

    def text1(self):
        re=self.element_text(search['拣货分播墙格子'])
        # print(re.split)
        str=re.split()[::2]
        return str
    def text2(self):
        re=self.element_text(search['满箱分播墙格子'])
        str=re.split('\n')
        list=[]
        # print(str)
        for i in range(int(len(str)/4)):
            list.append(str[4*i])
        return list

if __name__ == '__main__':
    pass
