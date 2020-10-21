# @Time:2020/10/13 14:59
# @Auth:Shuangqi.Cui
# @File:TestCases.py
# @IDE:PyCharm
import unittest
from time import sleep

from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.IndexPage import IndexPage
from Pages.NetworkParametersPage import NetworkParametersPage
from Pages.OpenVPNPage import OpenVPNPage
from Pages.SSTPPage import SSTPPage
from Pages.FirmwareUpdatePage import FirmwareUpdatePage


class TestIndexPage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print("自动化测试进行中...")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.url = BasePage.read_config()['url']
        # 执行前清空之前测试的配置信息
        with open('./common/ConfigInfo_UpdateBefore.yaml', mode='w') as f:
            f.write("")

    @classmethod
    def tearDownClass(cls):
        print("\n自动化测试已结束。")
        # cls.driver.quit()

    #    def setUp(self):
    #        print("方法 开始执行一次")
    #    def tearDown(self):
    #        print("方法 结束执行一次")

    # 进入首页
    def test001_Go_IndexPage(self):
        username = BasePage.read_config()['loginName']
        password = BasePage.read_config()['loginPassword']
        index_Page = IndexPage(self.driver, self.url)
        index_Page.goIndexPage()
        index_Page.click_risk_button()
        index_Page.input_username_password(username, password)
        index_Page.click_login_button()
        sleep(1)
        index_Page.click_close_prompt_box()
        # 断言应该配合固件升级前读取的信息
        self.assertEqual(index_Page.get_title(), "Xontel")

    def test002_Read_NetworkParametersPage(self):
        network_parameters = NetworkParametersPage(self.driver, self.url)
        network_parameters.click_network_button()
        sleep(1)
        network_parameters.click_network_parameters_button()
        network_info = network_parameters.read_network_configinfo()
        network_parameters.dict_to_yaml(network_info)

    def test003_Read_OpenVPNPage(self):
        openvpn = OpenVPNPage(self.driver, self.url)
        openvpn.click_vpn_client_button()
        sleep(1)
        openvpn.click_openvpn_button()
        sleep(1)
        openvpn_info = openvpn.read_openvpn_configinfo()
        if openvpn_info != "null":
            openvpn.dict_to_yaml(openvpn_info)

#    @unittest.skip("")
    def test004_Read_SSTPPage(self):
        sstp = SSTPPage(self.driver, self.url)
        sstp.click_sstp_button()
        sleep(1)
        sstp_info = sstp.read_sstp_configinfo()
        if sstp_info != "null":
            sstp.dict_to_yaml(sstp_info)

    # 未正是测试则跳过该用例
    @unittest.skip("跳过固件更新用例")
    def test088_FirmwareUpdate(self):
        firmware_update = FirmwareUpdatePage(self.driver, self.url)
        sleep(1)
        firmware_update.click_maintenance_button()
        sleep(1)
        firmware_update.click_firmware_update_button()
        sleep(1)
        firmware_update.firmware_update()
        update_result = firmware_update.is_update_success()
        if update_result == "success":
            # 更新成功等待重启
            reboot_flag = True
            while reboot_flag:
                try:
                    sleep(10)
                    self.test001_Go_IndexPage()
                    reboot_flag = False
                except:
                    print("即将进入系统...")
        else:
            # 更新失败
            print("更新失败！！！")

    #    固件更新完后，再次读取一遍配置信息，与yaml进行对比
    def test100_NetworkParameters(self):
        network_parameters = NetworkParametersPage(self.driver, self.url)
        # 不升级先不点这个
        # network_parameters.click_network_button()
        sleep(1)
        network_parameters.click_network_parameters_button()
        update_before_workmode = BasePage.update_before_config()['NetWorkParameters_WorkMode']
        update_after_workmode = network_parameters.get_network_work_mode()
        print("更新前网卡模式：" + update_before_workmode)
        self.assertEqual(update_before_workmode, update_after_workmode, "网卡模式")
        if update_before_workmode == "Single":
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_IPAddress'],
                             network_parameters.get_single_ipaddress())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_Mask'],
                             network_parameters.get_single_mask())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_GateWay'],
                             network_parameters.get_single_gateway())
        if update_before_workmode == "Double":
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_IPAddress1'],
                             network_parameters.get_double_ipaddress1())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_Mask1'],
                             network_parameters.get_double_mask1())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_GateWay1'],
                             network_parameters.get_double_gateway1())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_IPAddress2'],
                             network_parameters.get_double_ipaddress2())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_Mask2'],
                             network_parameters.get_double_mask2())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_GateWay2'],
                             network_parameters.get_double_gateway2())
        if update_before_workmode == "Bridge":
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_IPAddress'],
                             network_parameters.get_bridge_ipaddress())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_Mask'],
                             network_parameters.get_bridge_mask())
            self.assertEqual(BasePage.update_before_config()['NetWorkParameters_GateWay'],
                             network_parameters.get_bridge_gateway())
        print("升级后NetworkParameters 已读取")

    def test101_OpenVpn(self):
        openvpn = OpenVPNPage(self.driver, self.url)
        openvpn.click_vpn_client_button()
        sleep(1)
        openvpn.click_openvpn_button()
        sleep(1)
        update_after_client_ip = openvpn.get_client_ip()
        if update_after_client_ip != "null":
            update_before_client_ip = BasePage.update_before_config()['VPNClient_OpenVNP_ClientIP']
            self.assertEqual(update_before_client_ip, update_after_client_ip)
            print("升级后OpenVpn 已读取")

    def test102_SSTP(self):
        sstp = SSTPPage(self.driver, self.url)
        sstp.click_sstp_button()
        sleep(1)
        update_after_client_ip = sstp.get_client_ip()
        if update_after_client_ip != "null":
            update_before_client_ip = BasePage.update_before_config()['VPNClient_SSTP_ClientIP']
            self.assertEqual(update_before_client_ip, update_after_client_ip)