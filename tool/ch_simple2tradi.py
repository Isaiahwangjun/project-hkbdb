from opencc import OpenCC


def convert_text(data):

    converter = OpenCC('s2twp')

    # with open(path, 'r', encoding='utf-8') as file:
    #     data = json.load(file)

    if isinstance(data, str):
        return converter.convert(data)
    elif isinstance(data, dict):
        return {key: convert_text(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_text(item) for item in data]
    else:
        return data

    # with open('converted_json_file.json', 'w', encoding='utf-8') as file:
    #     json.dump(converted_data, file, ensure_ascii=False, indent=4)
