## 將 json 格式轉為 csv, 並將 lable 名稱正規化 (用 temp 資料夾裡面的模板定義)

import json
import pandas as pd
import importlib

# for windows
import sys

sys.path.append("../temp")


def to_csv():
    with open(r'modified_json_file.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with pd.ExcelWriter('杜漸regular.xlsx') as writer:
        for key, values in data.items():
            df = pd.DataFrame(values)

            try:
                # linux
                # temp_module = importlib.import_module(f"../temp.{key}")
                # windows
                temp_module = importlib.import_module(f"{key}",
                                                      package='../temp')
                temp = temp_module.get_temp()

                df.rename(columns=temp, inplace=True)
                df.to_excel(writer, sheet_name=key, index=False)

            except ModuleNotFoundError as e:
                df.to_excel(writer, sheet_name=key, index=False)
                print(e)


to_csv()
