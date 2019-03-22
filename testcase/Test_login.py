from selenium import webdriver
from common import LoginPage
import unittest


class BaiduSerch(unittest.TestCase):

    def test_baidu(self):
        dr = webdriver.Firefox()
        dr.get('https://www.baidu.com')
        bai = LoginPage(dr)
        bai.kw_send('selenium')
        bai.su_click()


if __name__ == '__main__':
    unittest.main()
