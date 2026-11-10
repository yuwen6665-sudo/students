

def add(records, item, raw):
    """录一条记录。raw 是金额原始字符串，校验全部在这里完成"""
    if not item:
        print("项目名称不能为空")
        return False
    if not raw.isdigit():
        print("金额必须是正整数")
        return False
    money = int(raw)
    if money <= 0:
        print("金额必须大于 0")
        return False
    records.append({"item": item, "money": money})
    print("已添加：%s %d 元" % (item, money))
    return True


def show_list(records):
    """打印任意记录列表，编号从 1 开始"""
    if not records:
        print("没有可显示的记录")
        return
    print("-" * 34)
    for i in range(len(records)):
        r = records[i]
        print("%d. %-10s %6d 元" % (i + 1, r["item"], r["money"]))
    print("-" * 34)


def show_all(records):
    if not records:
        print("还没有任何记录")
        return
    show_list(records)


def remove_by_index(records, idx):
    """按用户看到的编号删除（从 1 开始）"""
    if not (1 <= idx <= len(records)):
        print("编号超出范围（1 ~ %d）" % len(records))
        return False
    removed = records.pop(idx - 1)
    print("已删除：%s %d 元" % (removed["item"], removed["money"]))
    return True


def filter_by_item(records, keyword):
    """返回包含 keyword 的记录列表，不做任何打印"""
    if not keyword:
        return []
    return [r for r in records if keyword in r["item"]]


def sort_by_money(records, desc=True):
    """按金额原地排序"""
    if not records:
        print("还没有任何记录")
        return False
    records.sort(key=lambda r: r["money"], reverse=desc)
    return True


def get_stats(records):
    if not records:
        print("还没有记录，无法统计")
        return
    total = 0
    for r in records:
        total += r["money"]
    count = len(records)
    print("笔数：%d" % count)
    print("总支出：%d 元" % total)
    print("平均每笔：%.2f 元" % (total / count))


if __name__ == "__main__":
    rs = []
    add(rs, "苹果", "5")
    add(rs, "红富士苹果", "12")
    add(rs, "测试", "")          # 金额为空 → False
    add(rs, "测试", "abc")       # 非数字 → False
    show_all(rs)
    print("筛「苹果」结果：", filter_by_item(rs, "苹果"))
    print("筛「苹」结果  ：", filter_by_item(rs, "苹"))
    sort_by_money(rs, desc=True)
    show_all(rs)
    remove_by_index(rs, 1)
    show_all(rs)
    remove_by_index(rs, 99)      # 越界 → False
    get_stats(rs) 