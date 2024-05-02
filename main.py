from flask import Flask, jsonify, request
import json
from dotenv import load_dotenv
import os
from openai import OpenAI
import importlib
import openpyxl
import response
from datetime import datetime
from flask_cors import CORS
import threading
from tool import ch_simple2tradi, regularTime

app = Flask(__name__)
app.debug = True
CORS(app)

# 定義處理過程列表
all_processes = [
    "baseinfo", "nameinfo", "educate", "work", "publication", "article",
    "event", "honor", "organize", "piece", "relation"
]
# all_processes = [
#     "baseinfo", "nameinfo"]
name_value = 0
folder_name = 0


def try_parse_json(info):
    try:
        # 嘗試將 info 轉換為 Python 對象
        result = json.loads(info)
        return result
    except json.decoder.JSONDecodeError:
        return None


@app.route('/baseinfo', methods=['POST'])
def process_data_info():

    reciveData = request.json
    default = reciveData.get("default")

    if default != '':
        with open(f'{default}.json', 'r') as f:
            json_data = json.load(f)

        return jsonify(json_data)

    else:
        data = reciveData.get("data")
        load_dotenv()
        api_key = os.environ.get('OPENAI_API_KEY')
        client = OpenAI(api_key=api_key)

        module_name = f"prompt.baseinfo"
        prompt_module = importlib.import_module(module_name)

        user_message = """將下列文章填入格式中，並以json輸出: """ + data
        system_message, rule = prompt_module.get_prompt()

        response_ = response.create_completion(client, system_message,
                                               user_message, rule, process)

        # result = json.loads(response_.choices[0].message.content)
        result = try_parse_json(response_.choices[0].message.content)

        # 簡體轉繁體 & 正則化時間相關欄位
        result = ch_simple2tradi.convert_text(result)
        result = regularTime.modify_dates(result)

        basic_info = result.get('BasicInformation', [{}])[0]
        name_value = basic_info.get('常見名稱', basic_info.get('本名'))

        folder_name = f"{name_value}-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

        try:
            os.makedirs(f'./semantic_result/{folder_name}')
        except:
            pass

        json_path = f'./semantic_result/{folder_name}/baseinfo.json'

        with open(json_path, 'w', encoding='utf-8') as output:
            json.dump(result, output, ensure_ascii=False)

        ct = response_.usage.completion_tokens
        pt = response_.usage.prompt_tokens

        lock = threading.Lock()
        lock.acquire()
        try:
            wb = openpyxl.load_workbook('token.xlsx', data_only=True)

            sheet = wb['baseinfo']
            li = [folder_name, ct, ct * 0.03 / 1000, pt, pt * 0.01 / 1000]
            sheet.append(li)
            wb.save('token.xlsx')
            wb.close()
        finally:
            lock.release()

        return jsonify(result=result, folder_name=folder_name)


# 定義處理請求的路由函數
for process in all_processes:

    @app.route(f'/{process}',
               methods=['POST'],
               endpoint=f'process_data_{process}')
    def process_data(process=process):
        reciveData = request.json
        default = reciveData.get("default")

        if default != '':
            with open(f'{default}.json', 'r') as f:
                json_data = json.load(f)

            return jsonify(json_data)

        else:
            data = reciveData.get("data")
            folder_name = reciveData.get("folder_name")
            load_dotenv()
            api_key = os.environ.get('OPENAI_API_KEY')
            client = OpenAI(api_key=api_key)

            module_name = f"prompt.{process}"
            prompt_module = importlib.import_module(module_name)

            user_message = """將下列文章填入格式中，並以json輸出: """ + data
            system_message, rule = prompt_module.get_prompt()

            response_ = response.create_completion(client, system_message,
                                                   user_message, rule, process)

            # result = json.loads(response_.choices[0].message.content)
            result = try_parse_json(response_.choices[0].message.content)

            # 簡體轉繁體 & 正則化時間相關欄位
            result = ch_simple2tradi.convert_text(result)
            result = regularTime.modify_dates(result)

            # json_path = f'./semantic_result/{folder_name}/{process}.json'
            # with open(json_path, 'w', encoding='utf-8') as output:
            #     json.dump(result, output, ensure_ascii=False)

            ct = response_.usage.completion_tokens
            pt = response_.usage.prompt_tokens

            lock = threading.Lock()
            lock.acquire()
            try:
                wb = openpyxl.load_workbook('token.xlsx', data_only=True)

                sheet = wb[process]
                li = [folder_name, ct, ct * 0.03 / 1000, pt, pt * 0.01 / 1000]
                sheet.append(li)
                wb.save('token.xlsx')
                wb.close()
            finally:
                lock.release()

            # all_result = jsonCombine.combine(folder_name)

            return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
