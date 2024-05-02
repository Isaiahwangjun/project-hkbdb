import re


def modify_dates(data):

    # with open('converted_json_file.json', 'r', encoding='utf-8') as file:
    #     data = json.load(file)

    date_keys = ["出生日期", "開始時間", "結束時間", "出版日期", "日期"]
    if isinstance(data, dict):
        for key, value in data.items():
            if key in date_keys and isinstance(value, str):
                # 使用正则表达式提取数字部分并修改原始值
                data[key] = re.sub(r'\D', '', value)
            else:
                modify_dates(value)
    elif isinstance(data, list):
        for item in data:
            modify_dates(item)

    return data

    # with open('modified_json_file.json', 'w', encoding='utf-8') as file:
    #     json.dump(data, file, ensure_ascii=False, indent=4)
