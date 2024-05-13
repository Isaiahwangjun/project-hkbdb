import re
import json


def modify_dates(name):

    with open(
            f'C:/Users/wang/Desktop/daoyi/HongKong/capture100/{name}/all_result.json',
            'r',
            encoding='utf-8') as file:
        data = json.load(file)

    date_keys = ["出生日期", "開始時間", "結束時間", "出版日期", "日期"]

    # if isinstance(data, dict):
    #     for key, value in data.items():
    #         if key in date_keys and isinstance(value, str):
    #             # 使用正则表达式提取数字部分并修改原始值
    #             data[key] = re.sub(r'\D', '', value)
    #         else:
    #             modify_dates(value)
    # elif isinstance(data, list):
    #     for item in data:
    #         modify_dates(item)

    def modify_dates_recursively(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key in date_keys and isinstance(value, str):
                    # 使用正则表达式提取数字部分并修改原始值
                    data[key] = re.sub(r'\D', '', value)
                else:
                    modify_dates_recursively(value)
        elif isinstance(data, list):
            for item in data:
                modify_dates_recursively(item)

    modify_dates_recursively(data)

    with open(
            f'C:/Users/wang/Desktop/daoyi/HongKong/capture100/{name}/all_result.json',
            'w',
            encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
