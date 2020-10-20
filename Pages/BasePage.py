# @Time:2020/10/13 13:39
# @Auth:Shuangqi.Cui
# @File:BasePage.py
# @IDE:PyCharm


# pages基类
import os

import yaml


class BasePage(object):
    """
        Page基类，所有page都应该继承该类
    """
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # 查找元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 输入文本
    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    # 点击按钮
    def click(self, loc):
        self.find_element(*loc).click()

    # 元素存在则点击
    def is_click(self, loc):
        btn = self.find_element(*loc)
        if btn:
            btn.click()

    # 获取标题
    def get_title(self):
        return self.driver.title

    # 获取元素的text
    def get_element_text(self, loc):
        return self.find_element(*loc).text

    # 获取元素的value
    def get_element_value(self, loc):
        return self.find_element(*loc).get_attribute('value')

    # 单选框元素是否被勾选
    def is_checked(self, loc):
        return self.find_element(*loc).is_selected()

    # 读取配置文件
    @staticmethod
    def read_config():
        curPath = os.path.abspath(os.path.join(os.getcwd(), "./common"))
        yamlPath = os.path.join(curPath, "Config.yaml")
        with open(yamlPath, 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    # 将字典数据写入yaml配置文件中
    @staticmethod
    def dict_to_yaml(dict):
        curPath = os.path.abspath(os.path.join(os.getcwd(), "./common"))
        yamlPath = os.path.join(curPath, "ConfigInfo_UpdateBefore.yaml")
        with open(yamlPath, "a", encoding="utf-8") as f:
            yaml.dump(dict, f, default_flow_style=False, allow_unicode=True, indent=4)

    # 读取更新前的配置信息
    @staticmethod
    def update_before_config():
        curPath = os.path.abspath(os.path.join(os.getcwd(), "./common"))
        yamlPath = os.path.join(curPath, "ConfigInfo_UpdateBefore.yaml")
        with open(yamlPath, 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)