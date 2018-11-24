import os,sys
sys.path.append(os.getcwd())

from base.get_driver import get_driver
from page.page_login import PageLogin


class TestLogin():
    # 初始化方法
    def setup_class(self):
        # 实例化PageLogin
        self.login=PageLogin(get_driver())
    #结束方法
    def teardown_class(self):
        #关闭驱动对象
        self.login.driver.quit()
    def test_login(self,username="18366183691",password="123456"):
        #输入用户名
        self.login.page_input_usename(username)
        #输入密码
        self.login.page_input_password(password)
        #点击登录
        self.login.page_click_login_btn()


