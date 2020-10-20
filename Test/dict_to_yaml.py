# @Time:2020/10/13 17:50
# @Auth:Shuangqi.Cui
# @File:dict_to_yaml.py
# @IDE:PyCharm
import os
import yaml
# 将字典写入到yaml
my_dic = {
        'name': '张三',
        'sex': 'male',
        "address": "中国"
        }
curPath = os.path.abspath(os.path.join(os.getcwd(), "./common"))
print(curPath)
yamlPath = os.path.join(curPath, "ConfigInfo_UpdateBefore.yaml")
print(yamlPath)
# with open(yamlPath, "w", encoding="utf-8") as f:
#     yaml.dump(my_dic, f, default_flow_style=False, allow_unicode=True, indent=4)