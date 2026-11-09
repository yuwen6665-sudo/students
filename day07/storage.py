"""存储层：只负责 JSON 读写，不认识"记账"这回事"""

import json
import os


def save_records(records, path="records.json"):
    """把记录列表写进 JSON 文件。
    先写临时文件再原子替换，防止写一半崩溃导致原文件损坏。"""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def load_records(path="records.json"):
    """读回记录列表。文件不存在或内容损坏时返回 []，保证调用方永远能遍历。"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return data if isinstance(data, list) else []


if __name__ == "__main__":
    demo = [{"item": "午餐", "money": 25}, {"item": "晚餐", "money": 40}]
    save_records(demo, "records_test.json")
    got = load_records("records_test.json")
    print("读回:", got)
    print("长度:", len(got))
    print("往返一致:", got == demo)
    print("文件不存在:", load_records("不存在.json"))
    os.remove("records_test.json")