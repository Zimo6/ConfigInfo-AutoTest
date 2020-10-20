# @Time:2020/10/13 17:11
# @Auth:Shuangqi.Cui
# @File:FirmwareUpdatePage.py
# @IDE:PyCharm
import os
from time import sleep

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class FirmwareUpdatePage(BasePage):
    # 【元素集】
    # Maintenance 按钮
    maintenance_button = (By.XPATH, "//*[@href='index.php?menu=maintenance']/span")
    # Firmware Update 按钮
    firmware_update_button = (By.XPATH, "//*[@href='index.php?menu=backup_firmware']/span")
    # 固件文件
    firmware_file = (By.XPATH, "//*[@type='file']")
    # 选择升级按钮
    update_button = (By.XPATH, "//*[@id='sub']")
    # 确认升级按钮
    sure_update_button = (By.XPATH, "//*[@class='layui-layer-btn0']")
    # 更新提示信息
    update_message = (By.XPATH, "//*[@id='mgss']")
    # 关闭升级失败按钮
    update_fail_button = (By.XPATH, "//*[@id='modal-4']/div/div/div[1]/button")
    # 更新阶段信息
    update_phase_message = (By.XPATH, "//*[@id='modal-4']/div/div/div[2]/div/div[1]/span[1]")
    # 更新百分比信息
    update_percent_message = (By.XPATH, "//*[@id='cent']")
    # 确认立即重启按钮
    reboot_button = (By.XPATH, "//*[@onclick='react(2)']")
    # 固件路径
    firmware_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "./Firmware_File")), BasePage.read_config()['firmwareName'])

    def click_maintenance_button(self):
        self.click(self.maintenance_button)

    def click_firmware_update_button(self):
        self.click(self.firmware_update_button)

    # 固件升级
    def firmware_update(self):
        self.input_text(self.firmware_file, self.firmware_path)
        self.click(self.update_button)
        sleep(1)
        self.click(self.sure_update_button)
        sleep(1)

    # 判断是否更新成功(失败就截图，并终止后面操作)
    def is_update_success(self):
        if self.get_element_text(self.update_message) == "Files Upload format error":
            # 升级失败
            sleep(1)
            self.click(self.update_fail_button)
        else:
            # 升级中
            update_flag = True
            while update_flag:
                sleep(3)
                update_phase = self.get_element_text(self.update_phase_message)
                update_percentage = self.get_element_text(self.update_percent_message)
                print(f"第{update_phase}阶段已经更新{update_percentage}%...")
                if update_phase == "2" and update_percentage == "95":
                    print("更新成功，请等待系统重启")
                    sleep(8)
                    self.is_click(self.reboot_button)
                    update_flag = False
                    return "success"
                if self.get_element_text(self.update_message) == "Files Upload format error":
                    # 升级失败
                    sleep(1)
                    self.click(self.update_fail_button)
                    return "failed"

    # 升级完成后判断系统是否已经重启
    def is_reboot_success(self):
        if self.is_update_success() == "success":
            pass

