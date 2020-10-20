# @Time:2020/10/14 15:18
# @Auth:Shuangqi.Cui
# @File:SSTPPage.py
# @IDE:PyCharm
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class SSTPPage(BasePage):
    # 【元素集】
    # SSTP 按扭
    sstp_button = (By.XPATH, "//*[@href='index.php?menu=sstpvpn']/span")
    # Enable SSTP 单选框
    enable_sstp = (By.ID, "softethvpn")
    # Client IP
    client_ip = (By.ID, "service_ip")
    # Connect Status
    connect_status = (By.XPATH, '//*[@id="neo-contentbox-maincolumn"]/form/div[2]/div/div[11]/span/label[1]/span/font')

    def click_sstp_button(self):
        self.click(self.sstp_button)

    def get_client_ip(self):
        pass

    def read_sstp_configinfo(self):
        SSTP_Info = {}
        if self.is_checked(self.enable_sstp):
            now_connect_status = self.get_element_text(self.connect_status)
            while True:
                if now_connect_status == "" or now_connect_status == "Connecting":
                    print("等待连接中...")
                elif now_connect_status == "Failed":
                    return "null"
                elif now_connect_status == "Connected":
                    ci = self.get_element_text(self.client_ip)
                    SSTP_Info['VPNClient_SSTP_ClientIP'] = ci
                    print("SSTP_Info 配置信息已读取！")
                    print(SSTP_Info)
                    return SSTP_Info
        else:
            print("SSTP未开启，不会读取该配置信息！")
            return "null"