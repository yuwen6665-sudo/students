# ============================================================
#  D04 加练 · 记账本 v2（字典版）　【★★★】
# ------------------------------------------------------------
#  这是加速版第 1 天的核心任务。
#  昨天（v1 字符串版）用 "项目 金额" 存一条记录，统计时要 split 再转 int。
#  今天换成字典，你会亲眼看到代码短一半。
#
#  要求："""  """
#    1. 用 {"item": "午餐", "money": 25} 存每条记录，列表装多条
#    2. 拆 4 个函数：add_record / show_all / get_stats / main
#    3. 统计时直接 r["money"]，不许再 split 字符串
#    4. 输入校验：非数字、负数、空项目名都要挡住
#    5. 列表为空时统计不能除零
#
#  验收（自己走一遍）：
#    添加 3 笔 → 查看 3 条 → 统计正确 → 输入 abc 不崩 → 输入 5 不崩 → 退出
# ============================================================


def add_record(records):
    """添加一条记录，成功返回 True"""
    # ↓↓↓ 在这里写你的代码 ↓↓↓
    records.append()



# ↑↑↑ add_record 写完 ↑↑↑


def show_all(records):
    """逐条打印，带序号"""
    # ↓↓↓ 在这里写你的代码 ↓↓↓



# ↑↑↑ show_all 写完 ↑↑↑


def get_stats(records):
    """打印笔数、总支出、平均每笔"""
    # ↓↓↓ 在这里写你的代码 ↓↓↓



# ↑↑↑ get_stats 写完 ↑↑↑


def main():
    """菜单循环"""
    records = []
    # ↓↓↓ 在这里写你的代码 ↓↓↓
    # 提示：
    #   while True:
    #       打印菜单（1 添加 / 2 查看 / 3 统计 / 4 退出）
    #       choice = input("请选择：").strip()
    #       用 if / elif 分发到上面三个函数
    #       输入非 1-4 时提示"无效选项"



# ↑↑↑ main 写完 ↑↑↑


# ↓↓↓ 最后再取消这一行的注释（调通了才运行）↓↓↓
# main()


print()
print("=" * 50)
print("  骨架已给好，逐个函数填。填完先单独测每个函数，再跑 main()。")
print("=" * 50)


============================================================
                     参 考 答 案
         （做完再看。下面是注释，不会执行）
============================================================

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


def get_stats(records):
    if not records:
        print("还没有记录，无法统计")
        return
    total = 0
    for r in records:
        total += r["money"]        # ← 对比 v1：这里省掉了 split + int
    count = len(records)
    print("笔数：%d" % count)
    print("总支出：%d 元" % total)
    print("平均每笔：%.2f 元" % (total / count))


def main():
    records = []
    while True:
        print()
        print("===== 记账本 v2 =====")
        print("1. 添加记录")
        print("2. 查看全部")
        print("3. 统计")
        print("4. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_all(records)
        elif choice == "3":
            get_stats(records)
        elif choice == "4":
            print("再见")
            break
        else:
            print("无效选项，请输入 1-4")

main()


# ============================================================
#                   v1 和 v2 的差异（必读）
# ============================================================

# 【v1 · 字符串版】
#   records.append("午餐 25")
#   for r in records:
#       parts = r.split(" ")         # 要拆字符串
#       total += int(parts[1])       # 要转类型
#
# 【v2 · 字典版】
#   records.append({"item": "午餐", "money": 25})
#   for r in records:
#       total += r["money"]          # 直接取，不拆不转
#
# 少了 2 行，而且**更不容易错** —— v1 里如果项目名本身带空格（比如"晚餐 火锅 80"），
# parts[1] 就取错了。字典版完全没这个问题。
#
# 这就是「数据结构选对了，代码短一半」的真正含义：
# 不是少打字，是少出错。
#
# 以后你写 RAG 的文档片段，也是这个结构：
#   {"text": "原文片段", "source": "手册p12", "score": 0.87}
# 面试官问"你怎么存检索结果"，答这个结构就对了。
