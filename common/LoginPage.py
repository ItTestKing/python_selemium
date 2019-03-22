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
    username = (By.ID, "accountName")
    password = (By.ID, "password")
    dialoagButton = (By.XPATH, "//*[@id='loginform']/fieldset/div[3]/button")

    # get username textbox and input username

    def is_element_exist(self,css):
        s = self.driver.find_elements_by_css_selector(css_selector=css)
        if len(s) == 0:
            sleep(1)
            if len(s) == 1:
                return True
            else:
                print("元素未找到:%s" % css)
            return False
        elif len(s) == 1:
            return True

    def set_username(self, username):
        name = self.driver.find_element(*LoginPage.username)
        name.send_keys(username)
#        if self.is_element_exist("accountName"):
 #           print("meiy")

    # get password textbox and input password,then hit return
    def set_password(self, password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password)

    # Get "longin" button and then click
    def get_button(self):
        getbtn = self.driver.find_element(*LoginPage.dialoagButton)
        getbtn.click()
