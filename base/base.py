from selenium.webdriver.support.wait import WebDriverWait


class Base():
    #封装常用公共方法
    def __init__(self,driver):
        self.driver=driver

    #查找元素方法 封装
    def base_find_element(self,loc,timeout=30,poll=0.5):
        # *loc=By.XPATH,"//*[contains(....)]"
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # #2--- 下午详解
    # def base_find_element(self,loc):
    #     element=self.driver.find_element(*loc)
    #     return element

    # 点击元素 封装
    def base_click(self,loc):
        self.base_find_element(loc).click()
        el=self.base_find_element(loc)
        el.click()
    #2---下午详解
    # def base_click(self,loc):
    #     el=self.base_find_element(loc)
    #     el.click()
    # 输入方法 封装
    def base_input(self,loc,text):
        # 查找元素
        el=self.base_find_element(loc)
        #清除内容
        el.clear()
        # 输入内容
        el.send_keys(text)

