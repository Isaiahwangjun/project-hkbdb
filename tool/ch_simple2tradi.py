from opencc import OpenCC
import json


def convert_text(name):

    converter = OpenCC('s2twp')

    with open(
            f'C:/Users/wang/Desktop/daoyi/HongKong/capture100/{name}/all_result.json',
            'r',
            encoding='utf-8') as file:
        data = json.load(file)

    def convert_data(data):
        if isinstance(data, str):
            return converter.convert(data)
        elif isinstance(data, dict):
            return {key: convert_data(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [convert_data(item) for item in data]
        else:
            return data

    converted_data = convert_data(data)

    with open(
            f'C:/Users/wang/Desktop/daoyi/HongKong/capture100/{name}/all_result.json',
            'w',
            encoding='utf-8') as file:
        json.dump(converted_data, file, ensure_ascii=False, indent=4)
