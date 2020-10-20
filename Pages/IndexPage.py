# @Time:2020/10/13 13:47
# @Auth:Shuangqi.Cui
# @File:IndexPage.py
# @IDE:PyCharm
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class IndexPage(BasePage):
    # 【元素集】
    # 风险按钮
    risk_button1 = (By.ID, "details-button")
    risk_button2 = (By.ID, "proceed-link")
    # 用户名
    username = (By.XPATH, "//*[@name='input_user']")
    # 密码
    password = (By.XPATH, "//*[@name='input_pass']")
    # 登录按钮
    login_button = (By.XPATH, "//*[@name='submit_login']")
    # 修改密码提示框
    prompt_box = (By.XPATH, '//*[@id="modal-51"]/div/div/div[3]/button[2]')

    def __init__(self, driver, url):
        super().__init__(driver, url)

    # 进入首页
    def goIndexPage(self):
        print(f"打开网页：...{self.url}")
        self.driver.get(self.url)

    # 点击风险按钮(存在则点击)
    def click_risk_button(self):
        self.is_click(self.risk_button1)
        self.is_click(self.risk_button2)

    # 输入用户名和密码
    def input_username_password(self, username, password):
        self.input_text(self.username, username)
        self.input_text(self.password, password)

    # 点击登录按钮
    def click_login_button(self):
        self.click(self.login_button)

    # 点击关闭密码提示框
    def click_close_prompt_box(self):
        self.click(self.prompt_box)

