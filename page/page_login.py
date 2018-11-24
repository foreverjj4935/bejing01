from selenium.webdriver.common.by import By

from base.base import Base
loc_usename=(By.ID,"com.vcooline.aike:id/etxt_username")
loc_password=By.ID,"com.vcooline.aike:id/etxt_pwd"
loc_login_btn=By.ID,"com.vcooline.aike:id/btn_login"

class PageLogin(Base):
    # 调用使用self.loc_usename
    # loc_usename=(By.ID,"com.vcooline.aike:id/etxt_username")
    # loc_password=By.ID,"com.vcooline.aike:id/etxt_pwd"
    # loc_click=By.ID,"com.vcooline.aike:id/btn_login"
    #输入用户名
    def page_input_usename(self,text):
    #调用base类 封装的输入方法 ，因为继承Base ，所以直接通过self.xxx
        self.base_input(loc_usename,text)
    #输入密码
    def page_input_password(self,text):
        self.base_input(loc_password,text)
    #点击登录
    def page_click_login_btn(self):
        self.base_click(loc_login_btn)



