def get_temp():

    RelatedOrganizations_labels = {
        "組織名稱": "rdfs:label",
        "創立組織": "hasFounded",
        "成立地點": "hasLocationOfFormation",
        "參與組織": "hasParticipant",
        "地點": "hasPlace",
        "類型": "organizationType",
        "活動名稱": "activity",
        "開始時間": "hasStartDate",
        "結束時間": "hasEndDate",
        "職稱": "jobTitle",
        "時長": "period",
        "工作內容": "workingArea",
        "原始資料": "source"
    }

    return RelatedOrganizations_labels