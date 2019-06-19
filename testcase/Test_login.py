# coding:utf-8
from selenium import webdriver
import unittest
from common.LoginPage import LoginPage
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import unittest
import time
import common.LoginPage


class TestLogin(unittest.TestCase):

    # Setup
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options = option,desired_capabilities = None)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.driver.maximize_window()

    # tearDown
    def tearDown(self):
        print("用例执行成功")
        # self.driver.close()

    def test_Login(self):
        # Step1: open base site

        self.driver.get(self.base_url)
        # Step2: Open Login page
        login_page = LoginPage(self.driver)
        # Step3: Enter username

        login_page.set_username("sysadmin@mirror.com")
        # Step4: Enter password

        # Checkpoint1: Check popup dialog title
        # time.sleep(2)
        # Step5: Cancel dialog
        time.sleep(5)

        login_page.get_button()
        time.sleep(20)


# unittest.main()

if __name__ == "__main__":
    unittest.main()
