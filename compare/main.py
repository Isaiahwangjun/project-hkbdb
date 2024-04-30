import pandas as pd
from column_mapping import sheet_column_mapping
import oneDimension
import create_excel
import openpyxl


def fill0():
    workbook = openpyxl.load_workbook('Dustin-calculateAccu/score.xlsx')

    # 遍历每个工作表
    for sheet_name in workbook.sheetnames:
        # 获取当前工作表
        sheet = workbook[sheet_name]

        # 获取当前工作表的最大列数
        max_column = sheet.max_column

        # 获取当前工作表的最后一行的行号
        last_row_num = sheet.max_row

        # 获取当前工作表的最后一行的所有单元格
        last_row_cells = sheet[last_row_num]

        # 检查最后一行的每个单元格，如果为空则填充为0
        for cell in last_row_cells:
            if cell.value is None:
                cell.value = 0

    # 保存修改后的 Excel 文件
    workbook.save('Dustin-calculateAccu/score.xlsx')


def clear_excel(name, file):
    # delete empty sheets
    workbook = openpyxl.load_workbook(
        f'Dustin-calculateAccu/{name}/{file}.xlsx')

    for sheet_name in workbook.sheetnames:
        existing_data = pd.read_excel(
            f'Dustin-calculateAccu/{name}/{file}.xlsx', sheet_name=sheet_name)
        #  sheet 是否為空白或只有 header
        if existing_data.empty or len(existing_data) == 0:
            del workbook[sheet_name]
    workbook.save(f'Dustin-calculateAccu/{name}/{file}.xlsx')


def read_excel_files(name, sheets):
    data = None
    ans = None
    try:
        data = pd.read_excel(f'Dustin-calculateAccu/{name}/gpt.xlsx',
                             sheet_name=sheets)
    except:
        pass
    try:
        ans = pd.read_excel(f'Dustin-calculateAccu/{name}/hkbdb.xlsx',
                            sheet_name=sheets)
    except:
        pass
    return data, ans


def process_sheets(name, sheets):

    # 判断要執行一維還是二維分析
    if sheets in sheet_column_mapping.keys():
        data, ans = read_excel_files(name, sheets)
        # print(sheets)
        if data is None:
            if ans is not None:
                oneDimension.onlyhas_two(ans, sheets, name, 'HKBDBhas')
        elif ans is None:
            oneDimension.onlyhas_two(data, sheets, name, 'GPThas')
        else:
            oneDimension.diffWith2File_two(data, ans, sheets, name)
    else:
        # 如果不在 sheet_column_mapping 中，則進行一維分析
        data, ans = read_excel_files(name, sheets)
        if data is None:
            if ans is not None:
                oneDimension.onlyhas(ans, sheets, name, 'HKBDBhas')
        elif ans is None:
            oneDimension.onlyhas(data, sheets, name, 'GPThas')
        else:
            oneDimension.diffWith2File_one(data, ans, sheets, name)


def main(name):
    all_sheets = [
        "BasicInformation", "NameInformation", "Education", "Work",
        "Publication", "Article", "RelativeEvent", "Honor",
        "RelatedOrganizations", "Pieces", "Connections"
    ]

    create_excel.create(name)
    # create_excel.create_score()

    for sheets in all_sheets:
        process_sheets(name, sheets)


if __name__ == '__main__':
    name = '杜漸regular'
    clear_excel(name, 'gpt')
    clear_excel(name, 'hkbdb')
    main(name)
    fill0()
