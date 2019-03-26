# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.BasePages import BasePages
from time import sleep


class LoginPage(BasePages):
    '''
    这个类主要封装了，登录的find element 和操作事件。
    '''

    # page element identifier
    username = (By.ID, "kw")
    password = (By.ID, "su")

    # get username textbox and input username


    def set_username(self, username):
        name = self.driver.find_element(*LoginPage.username)
        name.send_keys(username)
#        if self.is_element_exist("accountName"):
 #           print("meiy")


    # Get "longin" button and then click
    def get_button(self):
        getbtn = self.driver.find_element(*LoginPage.password)
        getbtn.click()