## 將全部表單的結果合併在一起

import json
import os
import sys

file_list = [
    "baseinfo", "nameinfo", "educate", "work", "publication", "article",
    "piece", "organize", "relation", "event", "honor"
]


def combine(folder_name):
    combined_data = {}
    for filename in file_list:
        file_path = f'C:/Users/wang/Desktop/daoyi/HongKong/capture100/{folder_name}/{filename}.json'
        if os.path.exists(file_path):  # 確保檔案存在
            with open(file_path, encoding="utf-8") as file:
                data = json.load(file)
                if data is not None:
                    combined_data.update(data)  # 將資料附加到列表中

    with open(
            f'C:/Users/wang/Desktop/daoyi/HongKong/capture100/{folder_name}/all_result.json',
            'w',
            encoding="utf-8") as file:
        json.dump(combined_data, file, ensure_ascii=False)

    return combined_data


if __name__ == '__main__':
    print(sys.argv[1])
    combine(sys.argv[1])
