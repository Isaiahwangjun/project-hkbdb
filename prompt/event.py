import json


def get_prompt():
    example_json = {
        "RelativeEvent": [
            {
                "事件名稱": "",
                "地點": "地點1",
                "相關人物": "與誰有關",
                "相關組織": "與哪個組織有關",
                "開始時間": "日期的欄位請轉換成阿拉伯數字如一九九一年至一九九二:1991-1992",
                "結束時間": "日期的欄位請轉換成阿拉伯數字如一九九一年至一九九二:1991-1992",
                "時長": "",
                "作品": "作品1",
                "原始資料": ""
            },
        ]
    }

    system_message = """你是一位厲害的專欄記者和 json 格式大師，接下來會給你一段文章，並根據文章內容填入相關資訊，攸關於「Relative Event(相關事件)」，
    我們要調查作家與那些事件有關。如，"移居"、"訪問國家"、"企業上市"、"會見人物"、"留學" 等等會在新聞上看到的內容。
    資料格式應該像是: """ + json.dumps(example_json) + """。請確實找到文章內容再填入，資料正確很重要，
    一步一步慢慢做，即使多欄位空白也沒關係"""

    rule = """
    請遵循以下規則:
    1.以繁體中文回答
    2."原始資料" 請放文章內的引用，要簡短，不可超過20字。
    3.請不要將 "取得學位" 、"工作" 加入。
    4.專注於 「相關事件」如: 1.移居定居  2.訪問國家 3.企業上市 4.會見人物 5.留學 6.退休。
    5.無提及的欄位直接留空就好
    6.全部都沒有的話輸出"{}"，讓我可以解析json格式
    """

    return [system_message, rule]