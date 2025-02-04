import json
from datetime import datetime


def write_data_on_json(file_name,data):
    try:
        file_path = f"./assets/{file_name}.json"
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"File created successfully: {file_path}")
    except Exception as e:
        print(f"Error: {e}")
