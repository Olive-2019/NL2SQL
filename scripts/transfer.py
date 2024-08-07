import json

# 定义输出 JSON 数据到文件的函数
def write_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
# 定义读取 JSON 数据的函数
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 转换函数
def transform_data(source_data):
    transformed_data = []
    
    for item in source_data:
        conversation_entry = {
            "conversation": [
                {
                    "input": item["question"],
                    "output": item["query"]
                }
            ]
        }
        transformed_data.append(conversation_entry)
    
    return transformed_data
source_data = read_json_file("/root/NL2SQL/datas/dev.json")
# 执行转换
target_data = transform_data(source_data)

# 输出目标数据
write_json_file(target_data, "/root/NL2SQL/datas/dev_in_real_format.json")
print(json.dumps(target_data, indent=4, ensure_ascii=False))