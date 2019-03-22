from common import BasePages

class LoginPage(BasePages):
    kw = ['id', 'kw']  # 定位搜索输入框
    su = ['id', 'su']  # 搜索按钮

    def kw_send(self, value):  # 搜索框输入内容
        self.send(self.kw, value)

    def su_click(self):  # 点击搜索按钮
        self.click(self.su)


