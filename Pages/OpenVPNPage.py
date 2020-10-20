# @Time:2020/10/14 15:14
# @Auth:Shuangqi.Cui
# @File:OpenVPNPage.py
# @IDE:PyCharm
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class OpenVPNPage(BasePage):
    # 【元素集】
    # VPNClient 按钮
    vpn_client_button = (By.XPATH, "//*[@href='index.php?menu=vpn_client']/span")
    # OpenVPN 按钮
    openvpn_button = (By.XPATH, "//*[@href='index.php?menu=openvpn']/span")
    # Enable OpenVPN 单选框
    enable_openvpn = (By.ID, "openvpn")
    # OpenVPN Type
    openvpn_type = (By.XPATH, "//*[@id='cfg_mode']/option[@selected='selected']")
    # Client IP
    client_ip = (By.XPATH, "//*[@id='neo-contentbox-maincolumn']/form/div[2]/div[8]/span/label[2]/span")
    # Connect Status
    connect_status = (By.XPATH, "//*[@id='neo-contentbox-maincolumn']/form/div[2]/div[8]/span/label[1]/span/font")

    def click_vpn_client_button(self):
        self.click(self.vpn_client_button)

    def click_openvpn_button(self):
        self.click(self.openvpn_button)

    def get_client_ip(self):
        dict_client_ip = self.read_openvpn_configinfo()
        if dict_client_ip != "null":
            return dict_client_ip['VPNClient_OpenVNP_ServerIPAddress']
        else:
            return "null"

    def read_openvpn_configinfo(self):
        openVpn_Info = {}
        if self.is_checked(self.enable_openvpn):
            now_connect_status = self.get_element_text(self.connect_status)
            # 不需要判断类型
            # if self.get_element_text(self.openvpn_type) == "Manual Configuration":
            # 等待连接
            while True:
                if now_connect_status == "" or now_connect_status == "Connecting":
                    print("等待连接中...")
                elif now_connect_status == "Failed":
                    return "null"
                elif now_connect_status == "Connected":
                    ci = self.get_element_text(self.client_ip)
                    openVpn_Info['VPNClient_OpenVNP_ClientIP'] = ci
                    print("OpenVNP 配置信息已读取！")
                    print(openVpn_Info)
                    return openVpn_Info
        else:
            print("OpenVPN未开启，不会读取该配置信息！")
            return "null"
