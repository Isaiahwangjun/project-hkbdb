## 將 json 格式轉為 csv, 並將 lable 名稱正規化 (用 temp 資料夾裡面的模板定義)

import json
import pandas as pd
import importlib


def to_csv():
    with open('./semantic_result/江李志豪-2024-03-15_17-36-40/all_result.json',
              'r',
              encoding='utf-8') as f:
        data = json.load(f)

    with pd.ExcelWriter('output.xlsx') as writer:
        for key, values in data.items():

            df = pd.DataFrame(values)

            try:
                temp_module = importlib.import_module(f"../temp.{key}")
                temp = temp_module.get_temp()

                df.rename(columns=temp, inplace=True)
                df.to_excel(writer, sheet_name=key, index=False)

            except ModuleNotFoundError:
                df.to_excel(writer, sheet_name=key, index=False)


to_csv()
