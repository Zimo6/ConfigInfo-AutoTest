# @Time:2020/10/13 16:47
# @Auth:Shuangqi.Cui
# @File:NetworkParametersPage.py
# @IDE:PyCharm
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class NetworkParametersPage(BasePage):
    # 【元素集】
    # Network 按钮
    network_button = (By.XPATH, "//*[@href='index.php?menu=network']/span")
    # Network Parameters 按钮
    network_parameters_button = (By.XPATH, "//*[@href='index.php?menu=network_parameters']")
    # 当前选择网卡类型
    work_mode_selected = (By.XPATH, "//*[@id='workmode']/option[@selected]")
    # 【单网卡元素】
    single_ipaddress = (By.ID, "ip_eth0")
    single_mask = (By.ID, "mask_eth0")
    single_gateway = (By.ID, "gateway0")
    # 【双网卡元素】
    double_ipaddress1 = (By.ID, "ip_eth0")
    double_mask1 = (By.ID, "mask_eth0")
    double_gateway1 = (By.ID, "gateway0")
    double_ipaddress2 = (By.ID, "ip_eth1")
    double_mask2 = (By.ID, "mask_eth1")
    double_gateway2 = (By.ID, "gateway1")
    # 【桥接元素】
    bridge_ipaddress = (By.ID, "ip_br0")
    bridge_mask = (By.ID, "mask_br0")
    bridge_gateway = (By.ID, "gateway_br0")

    def click_network_button(self):
        self.click(self.network_button)

    def click_network_parameters_button(self):
        self.click(self.network_parameters_button)

    # 读取单个元素的信息
    def get_network_work_mode(self):
        return self.get_element_text(self.work_mode_selected)

    def get_single_ipaddress(self):
        return self.get_element_value(self.single_ipaddress)

    def get_single_mask(self):
        return self.get_element_value(self.single_mask)

    def get_single_gateway(self):
        return self.get_element_value(self.single_gateway)

    def get_double_ipaddress1(self):
        return self.get_element_value(self.double_ipaddress1)

    def get_double_mask1(self):
        return self.get_element_value(self.double_mask1)

    def get_double_gateway1(self):
        return self.get_element_value(self.double_gateway1)

    def get_double_ipaddress2(self):
        return self.get_element_value(self.double_ipaddress2)

    def get_double_mask2(self):
        return self.get_element_value(self.double_mask2)

    def get_double_gateway2(self):
        return self.get_element_value(self.double_gateway2)

    def get_bridge_ipaddress(self):
        return self.get_element_value(self.bridge_ipaddress)

    def get_bridge_mask(self):
        return self.get_element_value(self.bridge_mask)

    def get_bridge_gateway(self):
        return self.get_element_value(self.bridge_gateway)

    # 读取配置信息写入yaml
    def read_network_configinfo(self):
        # 网卡模式
        work_modes = ('Single', 'Double', 'Bridge')
        # 网络配置信息
        netWork_Info = {}
        # 获取当前网卡类型
        work_mode = self.get_element_text(self.work_mode_selected)
        print(f"当前网卡模式为：{work_mode}")
        netWork_Info["NetWorkParameters_WorkMode"] = work_mode
        if work_mode == work_modes[0]:
            # 【单网卡】
            ia = self.get_element_value(self.single_ipaddress)
            mask = self.get_element_value(self.single_mask)
            gw = self.get_element_value(self.single_gateway)
            # 存入字典中
            netWork_Info["NetWorkParameters_IPAddress"] = ia
            netWork_Info["NetWorkParameters_Mask"] = mask
            netWork_Info["NetWorkParameters_GateWay"] = gw
        elif work_mode == work_modes[1]:
            # 【双网卡】
            # 网口一
            ia1 = self.get_element_value(self.double_ipaddress1)
            mask1 = self.get_element_value(self.double_mask1)
            gw1 = self.get_element_value(self.double_gateway1)
            # 网口二
            ia2 = self.get_element_value(self.double_ipaddress2)
            mask2 = self.get_element_value(self.double_mask2)
            gw2 = self.get_element_value(self.double_gateway2)
            # 存入字典中
            netWork_Info["NetWorkParameters_IPAddress1"] = ia1
            netWork_Info["NetWorkParameters_Mask1"] = mask1
            netWork_Info["NetWorkParameters_GateWay1"] = gw1
            netWork_Info["NetWorkParameters_IPAddress2"] = ia2
            netWork_Info["NetWorkParameters_Mask2"] = mask2
            netWork_Info["NetWorkParameters_GateWay2"] = gw2
        elif work_mode == work_modes[2]:
            # 【桥接模式】
            ia = self.get_element_value(self.bridge_ipaddress)
            mask = self.get_element_value(self.bridge_mask)
            gw = self.get_element_value(self.bridge_gateway)
            # 存入字典中
            netWork_Info["NetWorkParameters_IPAddress"] = ia
            netWork_Info["NetWorkParameters_Mask"] = mask
            netWork_Info["NetWorkParameters_GateWay"] = gw
        print("NetWork Parameters 配置信息已读取！")
        print(netWork_Info)
        return netWork_Info
