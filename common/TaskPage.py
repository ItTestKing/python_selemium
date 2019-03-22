# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.BasePages import BasePages
from time import sleep

"""操作员界面"""

class TaskPage(BasePages):

#检测任务
    #检测任务
    task = (By.XPATH,"//*[@id='sidebar']/div[1]/div[1]/ul/li[3]/a/span")
    testingtask = (By.XPATH,"//*[@id='sidebar']/div[1]/div[1]/ul/li[3]/ul/li[1]/a")
    addtestingtask = (By.ID,"btnAdd")
    addtestingtask1 = ['id','btnAdd']
    searh = (By.ID,"btnSearch")
    searh1 = ['id','btnSearch']
    reset = (By.XPATH,"//*[@id='main-container']/div[2]/div/div[3]/div[2]/form/div[2]/button[2]")
    zhongduan = (By.XPATH,"//*[@id='taskForm']/div[6]/div/div/div[2]/input")



    #补丁任务
    patch = (By.XPATH,"//*[@id='sidebar']/div[1]/div[1]/ul/li[3]/ul/li[2]/a")
    addpatch = (By.ID,"btnAdd")
    strategySelecting = (By.ID,"strategySelecting")
    addstrateg = (By.XPATH,"//*[@id='179']")
    strategySelectingsure = (By.ID,"strategySelectingSure")


    #流量监控
    datamonitoring = (By.XPATH,"//*[@id='sidebar']/div[1]/div[1]/ul/li[3]/ul/li[3]/a")



    #处置任务
    disposaltask = (By.XPATH,"//*[@id='sidebar']/div[1]/div[1]/ul/li[3]/ul/li[4]/a")

    #检测任务
    def taskbtn(self):
        taskbtn = self.driver.find_element(*TaskPage.task)
        taskbtn.click()
    def testingtaskbtn(self):
        testingtaskbtn = self.driver.find_element(*TaskPage.testingtask)
        testingtaskbtn.click()
    def addtestingtaskbtn(self):

        addtestingtaskbtn = self.driver.find_element(*TaskPage.addtestingtask)
        addtestingtaskbtn.click()
      #  BasePages.click(self.addtestingtask1)

    def searchbtn(self):
        searchbtn = self.driver.find_element(*TaskPage.searh)
        searchbtn.click()
    def resetbtn(self):
        resetbtn = self.driver.find_element(*TaskPage.reset)
        resetbtn.click()
    def xuanquzhongduanbtn(self):
        zhongduanbt =self.driver.find_element(*self.zhongduan)
        zhongduanbt.click()

       # zhongduan = ["xpath", "//*[@id='taskForm']/div[6]/div/div/div[2]/input"]
      #  BasePages.click(zhongduan)

    # 补丁任务
    def patchbtn(self):
        patchbtn = self.driver.find_element(*TaskPage.patch)
        patchbtn.click()
    def addpatchcbtn(self):
        addpatchbtn =self.driver.find_element(*TaskPage.addpatch)
        addpatchbtn.click()
    def strategySelectingbtn(self):
        alert = self.driver.switch_to_alert()
        strategySelectingbtn = self.driver.find_element(*self.strategySelecting)
        strategySelectingbtn.click()
    def addstrtegbtn(self):
        addstratebtn = self.driver.find_element(*self.addstrateg)
        addstratebtn.click()
    def strtegyselectsurebtn(self):
        strategyselectsurebtn = self.driver.find_element(*self.strategySelectingsure)
        strategyselectsurebtn.click()