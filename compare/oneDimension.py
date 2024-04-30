import pandas as pd
from diff_match_patch import diff_match_patch
import importlib
from openpyxl.utils.dataframe import dataframe_to_rows
import openpyxl
from column_mapping import sheet_column_mapping
from fuzzywuzzy import fuzz
import DFappend
from score_mapping import sheet_score_mapping


def onlyhas(data, sheet, name, dcox):
    df = pd.DataFrame(columns=['key', 'value'])
    score_cnt = 0

    for _, row in data.iterrows():
        package = dynamic_import(sheet)
        for column in data.columns:
            if column in package.match_conditions:
                x = row[column]  # 从 data 中获取列的值
                df = DFappend.onlyGPTorHKBDBhasDF(df, column, x)
                score_cnt += 1

    mergeExcel(name, sheet, dcox, df)
    if dcox == 'HKBDBhas':
        writeInScoreExcel('onlyHKBDB', name, sheet, score_cnt)
    else:
        writeInScoreExcel('onlyGPT', name, sheet, score_cnt)


def onlyhas_two(data, sheet, name, dcox):
    df = pd.DataFrame(columns=['key', 'value', 'source'])
    sheet_columns = sheet_column_mapping.get(sheet, None)
    for _, row in data.iterrows():
        package = dynamic_import(sheet)
        for column in data.columns:
            if column in package.match_conditions:
                x = row[column]  # 从 data 中获取列的值
                df = DFappend.onlyGPTorHKBDBhasDF(df, column, x,
                                                  row[sheet_columns])
    mergeExcel(name, sheet, dcox, df)
    score_cnt = len(data)
    if dcox == 'HKBDBhas':
        writeInScoreExcel('onlyHKBDB', name, sheet, score_cnt)
    else:
        writeInScoreExcel('onlyGPT', name, sheet, score_cnt)


def dynamic_import(package_name):
    try:
        module = importlib.import_module(f"match_conditions.{package_name}")
        return module
    except ImportError:
        print(f"Failed to import module '{package_name}'")
        return None


def generate_diff(old_text, new_text):
    dmp = diff_match_patch()
    diffs = dmp.diff_main(old_text, new_text)
    dmp.diff_cleanupSemantic(diffs)
    diff_html = dmp.diff_prettyHtml(diffs)
    return diff_html


def mergeExcel(name, sheet, dcox, df):
    workbook = openpyxl.load_workbook(
        f"./Dustin-calculateAccu/{name}/{dcox}.xlsx")
    worksheet = workbook[sheet]

    for row in dataframe_to_rows(df, index=False, header=False):
        worksheet.append(row)
    worksheet.append([' ', ' '])
    workbook.save(f"./Dustin-calculateAccu/{name}/{dcox}.xlsx")


def writeInScoreExcel(type, name, sheet, score):
    workbook = openpyxl.load_workbook(f"./Dustin-calculateAccu/score.xlsx")
    worksheet = workbook[type]

    specific_column_index = None
    for i, cell in enumerate(worksheet[1]):  # 第一行是标题行
        if cell.value == sheet:
            specific_column_index = i + 1

    for row in worksheet.iter_rows(min_row=2, max_col=specific_column_index):
        if row[0].value == name:
            worksheet.cell(row=row[0].row,
                           column=specific_column_index,
                           value=score)
            workbook.save(f"./Dustin-calculateAccu/score.xlsx")
            return

    # 如果没有找到相同名称的行，则创建新行并添加分数
    max_row = worksheet.max_row
    worksheet.cell(row=max_row + 1, column=1, value=name)
    worksheet.cell(row=max_row + 1, column=specific_column_index, value=score)

    # 保存 Excel 文件
    workbook.save(f"./Dustin-calculateAccu/score.xlsx")


def diffWith2File_one(data, ans, sheet, name):

    match_total_cnt = 0  # 計算兩者都有的總欄位數
    match_gpt_score = 0  # 計算兩者的相似度 or 準確率
    GPTmore = 0
    GPTless = 0
    hkbdbCnt = len(ans)

    with open(f"./Dustin-calculateAccu/{name}/diff.html",
              "a",
              encoding='utf-8') as f:
        f.write(f"<h3>{sheet}</h3>")

    with open(f"./Dustin-calculateAccu/{name}/same.html",
              "a",
              encoding='utf-8') as f:
        f.write(f"<h3>{sheet}</h3>")

    diff_df = pd.DataFrame(columns=['key', 'GPT', 'HKBDB', 'score', 'source'])
    GPThas_df = pd.DataFrame(columns=['key', 'value', 'source'])
    HKBDBhas_df = pd.DataFrame(columns=['key', 'value', 'source'])

    for index, row in data.iterrows():
        y_row = ans.iloc[index]  # 使用 index 將 y_row 從 ans 中選取對應行

        package = dynamic_import(sheet)
        # 對於每個匹配條件，根據其鍵選取相應的匹配函數
        for condition_key, match_function in package.match_conditions.items():
            x = row.get(condition_key)  # 從 data 中取得 x 的值
            y = y_row.get(condition_key)  # 從 ans 中取得 y 的值

            # 處理三種情況：data 有而 ans 沒有、ans 有而 data 沒有、兩者都有
            if x is not None and y is not None:

                # 都有的話，計算準確率
                match_result = match_function(str(x), str(y))
                # print(f"{condition_key} 匹配結果:", match_result)

                # total accuracy
                match_total_cnt += 1
                match_gpt_score += match_result / 100

                # 如果有差異，將差異的部分呈現 html &　excel
                if match_result != 100:
                    diff_html = generate_diff(str(x), str(y))
                    diff_html_with_info = f"{condition_key}: {diff_html} ({match_result})<br>"
                    with open(f"./Dustin-calculateAccu/{name}/diff.html",
                              "a",
                              encoding='utf-8') as f:
                        f.write(diff_html_with_info)
                        f.write('\n')

                    diff_df = DFappend.diffDF(diff_df, condition_key, x, y,
                                              match_result)
                else:  #如果相似度 = 100, 網頁呈現
                    html_info = f"{condition_key} <span style='background-color: rgba(255, 0, 0, 0.3);'>{x} </span> <span style='background-color: rgba(0, 255, 0, 0.3);'>{y}</span><br>"
                    with open(f"./Dustin-calculateAccu/{name}/same.html",
                              "a",
                              encoding='utf-8') as f:
                        f.write(html_info)
                        f.write('\n')

            elif x is not None and y is None:
                if not pd.isna(x):
                    # print(f"{condition_key} GPT有， HKDBD沒有")
                    GPThas_df = DFappend.onlyGPTorHKBDBhasDF(
                        GPThas_df, condition_key, x)
                    GPTmore += 1

            elif x is None and y is not None:
                if not pd.isna(y):
                    # print(f"{condition_key} HKBDB有， GPT沒有")
                    HKBDBhas_df = DFappend.onlyGPTorHKBDBhasDF(
                        HKBDBhas_df, condition_key, y)
                    GPTless += 1

    writeInScoreExcel('accuracy', name, sheet,
                      (match_gpt_score / match_total_cnt))
    writeInScoreExcel('onlyGPT', name, sheet, (GPTmore / hkbdbCnt))
    writeInScoreExcel('onlyHKBDB', name, sheet, (GPTless / hkbdbCnt))

    mergeExcel(name, sheet, 'diff', diff_df)
    mergeExcel(name, sheet, 'GPThas', GPThas_df)
    mergeExcel(name, sheet, 'HKBDBhas', HKBDBhas_df)

    # match_accuracy = match_gpt_score / match_total_cnt
    # print(match_accuracy)


def diffWith2File_two(data, ans, sheet, name):

    match_total_cnt = 0  # 計算兩者都有的總欄位數
    match_gpt_score = 0  # 計算兩者的相似度 or 準確率
    GPTmore = 0
    GPTless = 0

    with open(f"./Dustin-calculateAccu/{name}/diff.html",
              "a",
              encoding='utf-8') as f:
        f.write(f"<h3>{sheet}</h3>")

    with open(f"./Dustin-calculateAccu/{name}/same.html",
              "a",
              encoding='utf-8') as f:
        f.write(f"<h3>{sheet}</h3>")

    diff_df = pd.DataFrame(columns=['key', 'GPT', 'HKBDB', 'score', 'source'])
    GPThas_df = pd.DataFrame(columns=['key', 'value', 'source'])
    HKBDBhas_df = pd.DataFrame(columns=['key', 'value', 'source'])

    sheet_columns = sheet_column_mapping.get(sheet, None)
    EachCellScore = float(sheet_score_mapping.get(sheet, None))

    unmatched_data = pd.DataFrame()  # 存储未匹配到的 data 行
    unmatched_ans = ans.copy()  # 創建 ans 的副本用於追蹤未匹配的行

    hkbdbCnt = len(unmatched_ans)  # 計算 (gpt有hkbdb沒有 or hkbdb有gpt沒有) 的分母

    # 根据某一列的字符串长度对 DataFrame 进行排序
    data = data.sort_values(by=data.columns[0],
                            key=lambda x: x.str.len(),
                            ascending=False)
    ans = ans.sort_values(by=ans.columns[0],
                          key=lambda x: x.str.len(),
                          ascending=False)

    for _, row_data in data.iterrows():
        best_match_ratio = -1  # 最佳匹配相似度
        best_match_row_ans = None  # 最佳匹配的 ans 行

        # 遍历 ans 的每一行
        for _, row_ans in unmatched_ans.iterrows():
            # 计算当前行与 data 行的相似度
            similarity_ratio = fuzz.ratio(str(row_data[sheet_columns]),
                                          str(row_ans[sheet_columns]))

            # 更新最佳匹配
            if similarity_ratio > 50:
                if similarity_ratio > best_match_ratio:
                    best_match_ratio = similarity_ratio
                    best_match_row_ans = row_ans
        # print(row_data[0], best_match_row_ans[0])
        # 如果找到了最佳匹配行，從未匹配的 ans 列表中刪除該行
        if best_match_row_ans is not None:
            unmatched_ans = unmatched_ans.drop(best_match_row_ans.name)
        else:
            unmatched_data = unmatched_data._append(row_data)
            continue

        package = dynamic_import(sheet)
        # 比较数据并存储差异信息
        for condition_key, match_function in package.match_conditions.items():
            x = row_data.get(condition_key)
            y = best_match_row_ans.get(condition_key)

            # 處理三種情況：data 有而 ans 沒有、ans 有而 data 沒有、兩者都有
            if pd.notnull(x) and pd.notnull(y):
                # 都有的话，计算准确率
                match_result = match_function(str(x), str(y))
                # print(f"{condition_key} {x} {y}  匹配結果:", match_result)

                # total accuracy
                match_total_cnt += 1
                match_gpt_score += match_result / 100

                # 如果有差異，將差異的部分存入 diff_df
                if match_result != 100:
                    diff_html = generate_diff(str(x), str(y))
                    diff_html_with_info = f"{condition_key}: {diff_html} ({match_result})<br>"
                    with open(f"./Dustin-calculateAccu/{name}/diff.html",
                              "a",
                              encoding='utf-8') as f:
                        f.write(diff_html_with_info)
                        f.write('\n')
                    diff_df = DFappend.diffDF(
                        diff_df, condition_key, x, y, match_result,
                        str(best_match_row_ans[sheet_columns]))

                else:  #如果相似度 = 100, 網頁呈現
                    html_info = f"{condition_key} <span style='background-color: rgba(255, 0, 0, 0.3);'>{x} </span> <span style='background-color: rgba(0, 255, 0, 0.3);'>{y}</span><br>"
                    with open(f"./Dustin-calculateAccu/{name}/same.html",
                              "a",
                              encoding='utf-8') as f:
                        f.write(html_info)
                        f.write('\n')

            #4/29 接著做 data 有而 ans 沒有、ans 有而 data 沒有
            elif pd.notnull(x):
                GPTmore += EachCellScore
                # print(
                #     f"{best_match_row_ans[sheet_columns]} {condition_key} GPT有， HKDBD沒有"
                # )
                GPThas_df = DFappend.onlyGPTorHKBDBhasDF(
                    GPThas_df, condition_key, x,
                    str(best_match_row_ans[sheet_columns]))

            elif pd.notnull(y):
                GPTless += EachCellScore
                # print(
                #     f"{best_match_row_ans[sheet_columns]} {condition_key} HKBDB有， GPT沒有"
                # )
                HKBDBhas_df = DFappend.onlyGPTorHKBDBhasDF(
                    HKBDBhas_df, condition_key, y,
                    str(best_match_row_ans[sheet_columns]))

    for _, row_data in unmatched_data.iterrows():
        GPTmore += 1
        package = dynamic_import(sheet)
        for condition_key, match_function in package.match_conditions.items():
            x = row_data.get(condition_key)
            if pd.notnull(x):
                GPThas_df = DFappend.onlyGPTorHKBDBhasDF(
                    GPThas_df, condition_key, x, str(row_data[sheet_columns]))

    for _, row_data in unmatched_ans.iterrows():
        GPTless += 1
        package = dynamic_import(sheet)
        for condition_key, match_function in package.match_conditions.items():
            x = row_data.get(condition_key)
            if pd.notnull(x):
                HKBDBhas_df = DFappend.onlyGPTorHKBDBhasDF(
                    HKBDBhas_df, condition_key, x,
                    str(row_data[sheet_columns]))

    writeInScoreExcel('accuracy', name, sheet,
                      (match_gpt_score / match_total_cnt))
    writeInScoreExcel('onlyGPT', name, sheet, (GPTmore / hkbdbCnt))
    writeInScoreExcel('onlyHKBDB', name, sheet, (GPTless / hkbdbCnt))

    mergeExcel(name, sheet, 'diff', diff_df)
    mergeExcel(name, sheet, 'GPThas', GPThas_df)
    mergeExcel(name, sheet, 'HKBDBhas', HKBDBhas_df)
