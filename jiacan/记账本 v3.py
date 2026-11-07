# `add` / `remove_by_index` / `filter_by_item` / `sort_by_money` / `get_stats`）复制过来，然后写 `main()` 串起来。
# ===== 记账本 v3 =====
# 1. 添加记录
# 2. 查看全部
# 3. 删除记录
# 4. 按项目筛选
# 5. 按金额排序
# 6. 统计
# 7. 保存到文件（晚上学完再加）
# 8. 退出

def add_record(records):
    item = input("请输入项目名称：").strip()
    if not item:
        print("项目名称不能为空")
        return False

    raw = input("请输入金额：").strip()
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

def show_all(records):
    if not records:
        print("还没有任何记录")
        return
    print("-" * 34)
    for i in range(len(records)):
        r = records[i]
        print("%d. %-10s %6d 元" % (i + 1, r["item"], r["money"]))
    print("-" * 34)

def del_record(records):
    if not records:
        print("还没有任何记录，无法删除")
        return
    show_all(records)
    raw = input("请输入要删除的记录序号：").strip()
    if not raw.isdigit():
        print("请输入有效的序号")
        return
    index = int(raw) - 1
    if index < 0 or index >= len(records):
        print("序号超出范围")
        return
    removed = records.pop(index)
    print("已删除：%s %d 元" % (removed["item"], removed["money"]))

def shaixuan(records):
    if not records:
        print("还没有任何记录，无法筛选")
        return False
    keyword = input("请输入你要筛查的项目名").strip()
    if not keyword:
        print("项目名称不能为空")
        return False
    found = 0
    for i in range(len(records)):
        r = records[i]
        if keyword==records[i]["item"]:
            found+=1
            print("%d. %-10s %6d 元" % (i+1, r["item"], r["money"]))
    if found == 0:
        print("没有该项目")
        return False

def paixun(records):
    if not records:
        print("还没有任何记录，无法排序")
        return False
    while True:
        way = input("请输入1或2。\n1.从大到小排序。\n2.从小到大排序。").strip()
        if way not in ("1","2"):
            print("输入错误，请输入1或2")
            continue
        records.sort(key=lambda r: r["money"], reverse=(way == "1"))
        break
    print("已按金额%s排序" % ("从大到小" if way == "1" else "从小到大"))
    show_all(records)




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

def save_to_file(records):
    if not records:
        print("没有记录可保存")
        return
    fname = "records.txt"
    with open(fname, "w", encoding="utf-8") as f:
        for r in records:
            f.write("%s|%d\n" % (r["item"], r["money"]))
    print("已保存 %d 条到 %s" % (len(records), fname))



def main():
    records = []
    while True:
        print()
        print("===== 记账本 v2 =====")
        print("1. 添加记录")
        print("2. 查看全部")
        print("3. 删除记录")
        print("4. 按项目筛选")
        print("5. 按金额排序")
        print("6. 统计")
        print("7. 保存到文件")
        print("8. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_all(records)
        elif choice == "3":
            del_record(records)
        elif choice == "4":
            shaixuan(records)
        elif choice == "5":
            paixun(records)
        elif choice == "6":
             get_stats(records)
        elif choice == "7":
            save_to_file(records)
        elif choice == "8":
            print("再见")
            break
        else:
            print("无效选项，请输入 1-8")

main()