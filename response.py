def create_completion(client, system_message, user_message, rule,
                      process_type):
    # 定義每個處理方式的預設值
    default_temperatures = {
        "baseinfo": 0.5,
        "nameinfo": 0.8,
        "educate": 0.5,
        "work": 0.5,
        "publication": 0.5,
        "article": 0,
        "event": 0.5,
        "honor": 0.5,
        "organize": 0.2,
        "piece": 0.2,
        "relation": 0,
    }

    # 獲取處理方式對應的預設值
    default_temperature = default_temperatures.get(process_type, 0.5)

    # 調用 OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=default_temperature,
        response_format={"type": "json_object"},
        messages=[{
            "role": "system",
            "content": system_message
        }, {
            "role": "user",
            "content": user_message
        }, {
            "role": "user",
            "content": rule
        }])

    return response
