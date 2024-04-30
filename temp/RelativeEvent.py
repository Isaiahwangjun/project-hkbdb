def get_temp():

    RelativeEvent_labels = {
        "事件名稱": "rdfs:label",
        "地點": "hasEventPlace",
        "相關人物": "hasRelatedPerson",
        "相關組織": "hasRelatedOrganization",
        "開始時間": "hasStartDate",
        "結束時間": "hasEndDate",
        "時長": "period",
        "作品": "work",
        "原始資料": "source"
    }

    return RelativeEvent_labels
