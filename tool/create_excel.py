## 用來產生計算價格的空白 excel

import openpyxl

file_list = [
    "baseinfo", "nameinfo", "educate", "work", "publication", "article",
    "piece", "organize", "relation", "event", "honor"
]

# 創建一個新的 Excel 工作簿
workbook = openpyxl.Workbook()

# 添加 11 個表單
for i in file_list:
    worksheet = workbook.create_sheet(title=i)

    # 添加欄位名稱
    worksheet['A1'] = '作家'
    worksheet['B1'] = 'asnwer_token'
    worksheet['C1'] = 'price'
    worksheet['D1'] = 'promp_toke'
    worksheet['E1'] = 'price'

# 移除預設的 Sheet
workbook.remove(workbook['Sheet'])

# 儲存 Excel 文件
workbook.save('token.xlsx')
