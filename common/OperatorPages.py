# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.BasePages import BasePages
from time import sleep

"""操作员界面"""

class OperatorPages(BasePages):

#概览
    #概览标签
    gailan = (By.XPATH,"//*[@id='sidebar']/div[1]/div[1]/ul/li[1]/a/span")
    yizhou = (By.XPATH,"//*[@id='main-container']/div[2]/div/div[3]/div[1]/div/ul/li[1]/a")
    yiyue = (By.XPATH,"//*[@id='main-container']/div[2]/div/div[3]/div[1]/div/ul/li[2]/a")
    yijidu = (By.XPATH,"//*[@id='main-container']/div[2]/div/div[3]/div[1]/div/ul/li[3]/a")
    gaowei = (By.ID,"blackCount")
    keyi = (By.ID,"unkonwnCount")
    zhengchang = (By.ID,"unkonwnCount")
    chakan = (By.XPATH,"//*[@id='dlshouwen_grid_69ec382f971940a5f281983c047c080b'']/tbody/tr[3]/td[12]")



    def gailanbtn(self):
        gailanbtn = self.driver.find_element(*OperatorPages.gailan)
        gailanbtn.click()
    def yizhou(self):
        yizhoubtn = self.driver.find_element(*OperatorPages.yizhou)
        yizhoubtn.click()
    def yiyuebtn(self):
        yiyuebtn = self.driver.find_element(*OperatorPages.yiyue)
        yiyuebtn.click()
    def yijidubtn(self):
        yijidubtn = self.driver.find_element(*OperatorPages.yijidu)
        yijidubtn.click()
    def gaoweibtn(self):
        gaoweibtn = self.driver.find_element(*OperatorPages.gaowei)
        gaoweibtn.click()
    def keyibtn(self):
        keyibtn = self.driver.find_element(*OperatorPages.keyi)
        keyibtn.click()
    def zhengchangbtn(self):
        zhengchangbtn = self.driver.find_element(*OperatorPages.zhengchang)
        zhengchangbtn.click()

    def chakanbtn(self):
        chakanbtn = self.driver.find_element(*OperatorPages.chakan)
        chakanbtn.click()
