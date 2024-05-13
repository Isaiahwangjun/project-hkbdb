def get_temp():

    Work_labels = {
        # "工作名稱": "rdfs:label",
        "工作類型": "employmentType",
        "工作名稱": "jobTitle",
        # "職稱": "jobTitle",
        "地點": "hasPlace",
        "工作地點": "hasPlace",
        "工作於": "hasEmployedAt",
        "引薦者": "hasAlumni",
        "開始時間": "hasStartDate",
        "結束時間": "hasEndDate",
        "欄目名稱": "column",
        "專欄類型": "hasGenre",
        "專欄合寫者": "hasColumnist",
        "筆名": "penName",
        "時長": "period",
        "活動名字": "activity",
        "工作內容": "workingArea",
        "原始資料": "source"
    }

    return Work_labels
