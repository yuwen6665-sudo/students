# ============================================================
#  D04 练习 · 函数 + 列表（5 道，最后一道是完整小程序）
#  难度：★ 基础 / ★★ 进阶 / ★★★ 挑战
# ------------------------------------------------------------
#  用法：一次一题，做完运行，对照验收；做完一题整段 Ctrl + / 注释掉。
#  硬要求：每题自己造 3 组边界输入（0、负数、空列表、极大值、非数字）
# ============================================================


# ============================================================
#  第 1 题 · 带默认值的四则运算　【★ 基础】
# ------------------------------------------------------------
#  calc(a, b, op="+")，支持 + - * /
#  除法时 b 为 0 → 返回「除数不能为 0」
#  不认识的 op → 返回「不支持的运算」
#  验收：calc(6,3)=9 ／ calc(6,3,"/")=2.0 ／ calc(6,0,"/")=除数不能为 0
#  提示：默认参数 + 卫语句（提前 return）
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓

# def calc(a, b, op="+"):
#     if op == "+":
#         return a + b
#     elif op == "-":
#         return a - b
#     elif op == "*":
#         return a * b
#     elif op == "/":
#         if b == 0:
#             return "除数不能为 0"
#         return a / b
#     else:
#         return "不支持的运算"

# ↑↑↑ 第 1 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 1 题 结束", "=" * 46)


# ============================================================
#  第 2 题 · 列表基本操作　【★ 基础】
# ------------------------------------------------------------
#  空列表 → append "语文" "数学" "英语"
#  → insert(1, "物理") → remove("英语") → 打印列表和长度
#  验收：['语文', '物理', '数学']，长度 3
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓

# lest=[]
# lest.append("语文")
# lest.append("数学")
# lest.append("英语")
# lest.insert(1, "物理")
# lest.remove("英语")
# print(lest)
# print(len(lest))

# ↑↑↑ 第 2 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 2 题 结束", "=" * 46)


# ============================================================
#  第 3 题 · 求和与平均（函数调函数）　【★★ 进阶】
# ------------------------------------------------------------
#  total(lst) 不许用 sum()；average(lst) 调用 total，保留 2 位
#  空列表都返回 0
#  验收：[80,90,75] → 245 / 81.67；[] → 0 / 0
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓



# ↑↑↑ 第 3 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 3 题 结束", "=" * 46)


# ============================================================
#  第 4 题 · 找最大最小（不用 max/min）　【★★ 进阶】
# ------------------------------------------------------------
#  find_max(lst) / find_min(lst)，空列表返回 None
#  验收：[3,9,2] → 9/2；[-5,-8,-2] → -2/-8；[] → None/None
#  提示：初始值用 lst[0]，先用 if 判断空
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓

# def find_max(lst):
#     if not lst:
#         return None
#     max_val = lst[0]
#     for n in lst:
#         if n > max_val:
#             max_val = n
#     return max_val

# def find_min(lst):
#     if not lst:
#         return None
#     min_val = lst[0]
#     for n in lst:
#         if n < min_val:
#             min_val = n
#     return min_val

# ↑↑↑ 第 4 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 4 题 结束", "=" * 46)


# ============================================================
#  第 5 题 · 完整小程序：命令行记账本 v1　【★★★ 挑战】
# ------------------------------------------------------------
#  这是今天最重要的一道 —— 从「写一个函数」升级到「写一个能用的工具」
#
#  功能（用 while True + 菜单循环）：
#    1. 添加记录：输入"项目 金额"，存进列表（例：午餐 25）
#    2. 查看全部：逐条打印，带序号
#    3. 统计：总支出、平均每笔、笔数
#    4. 退出
#
#  硬要求（每条都是真实工程要求）：
#    ① 至少 4 个函数：add_record / show_all / get_stats / main
#    ② 金额必须是正数，非数字或负数 → 提示后重新输入，不许崩
#    ③ 统计时列表为空要能处理（不能除零）
#    ④ 菜单输入非 1-4 时提示"无效选项"
#
#  验收（自己走一遍）：
#    添加 3 笔 → 查看 3 条 → 统计正确 → 输入 abc 不崩 → 输入 5 不崩 → 退出
#
#  提示：
#    records = []                      记录存在这里
#    records.append("午餐 25")          先存字符串也行
#    想拆金额：s.split(" ") → ["午餐","25"]，再 int()
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓

def add_record(records):
    """添加一条记录，返回 True 表示成功"""
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
    records.append("%s %d" % (item, money))
    print("已添加：%s %d 元" % (item, money))
    return True

def show_all(records):
    if not records:
        print("还没有任何记录")
        return
    print("-" * 30)
    for i in range(len(records)):
        print("%d. %s" % (i + 1, records[i]))
    print("-" * 30)

def get_stats(records):
    if not records:
        print("还没有记录，无法统计")
        return
    total = 0
    for r in records:
        parts = r.split(" ")
        total += int(parts[1])
    count = len(records)
    print("笔数：%d" % count)
    print("总支出：%d 元" % total)
    print("平均每笔：%.2f 元" % (total / count))

records=[]
while True:
    print("\n=== 命令行记账本 v1 ===")
    print("1. 添加记录")
    print("2. 查看全部")
    print("3. 统计")
    print("4. 退出")
    choice = input("请选择操作：").strip()

    if choice == "1":
        add_record(records)
    elif choice == "2":
        show_all(records)
    elif choice == "3":
        get_stats(records)
    elif choice == "4":
        print("感谢使用，再见！")
        break
    else:
        print("无效选项，请重新输入。")

# ↑↑↑ 第 5 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 5 题 结束", "=" * 46)


print()
print("5 题全部完成。第 5 题能跑通，你今天就真的上了一个台阶。")


# ============================================================
#                      参 考 答 案
#          （做完了再看。下面是注释，不会执行）
# ============================================================

# ---- 第 1 题 ----
# def calc(a, b, op="+"):
#     if op == "+":
#         return a + b
#     elif op == "-":
#         return a - b
#     elif op == "*":
#         return a * b
#     elif op == "/":
#         if b == 0:
#             return "除数不能为 0"
#         return a / b
#     else:
#         return "不支持的运算"
#
# 讲评：每个分支都 return，所以不需要 else 嵌套；除法先判 0 = 卫语句。

# ---- 第 2 题 ----
# subjects = []
# subjects.append("语文")
# subjects.append("数学")
# subjects.append("英语")
# subjects.insert(1, "物理")
# subjects.remove("英语")
# print(subjects)        # ['语文', '物理', '数学']
# print(len(subjects))   # 3
#
# 讲评：四个方法都是原地修改，千万别写 subjects = subjects.append(...)

# ---- 第 3 题 ----
# def total(lst):
#     if not lst:
#         return 0
#     s = 0
#     for n in lst:
#         s += n
#     return s
#
# def average(lst):
#     if not lst:
#         return 0
#     return round(total(lst) / len(lst), 2)
#
# 讲评：average 调用 total，这就是「函数复用」。如果平均分再自己写一遍求和，
#      以后改求和逻辑就要改两处 —— 这是要避免的。

# ---- 第 4 题 ----
# def find_max(lst):
#     if not lst:
#         return None
#     m = lst[0]
#     for n in lst:
#         if n > m:
#             m = n
#     return m
#
# def find_min(lst):
#     if not lst:
#         return None
#     m = lst[0]
#     for n in lst:
#         if n < m:
#             m = n
#     return m
#
# 讲评：初始值用 lst[0] 而不是 0 —— 全负数时用 0 会错。

# ---- 第 5 题 参考答案（完整小程序）----
# def add_record(records):
#     """添加一条记录，返回 True 表示成功"""
#     item = input("请输入项目名称：").strip()
#     if not item:
#         print("项目名称不能为空")
#         return False
#     raw = input("请输入金额：").strip()
#     if not raw.isdigit():
#         print("金额必须是正整数")
#         return False
#     money = int(raw)
#     if money <= 0:
#         print("金额必须大于 0")
#         return False
#     records.append("%s %d" % (item, money))
#     print("已添加：%s %d 元" % (item, money))
#     return True
#
# def show_all(records):
#     if not records:
#         print("还没有任何记录")
#         return
#     print("-" * 30)
#     for i in range(len(records)):
#         print("%d. %s" % (i + 1, records[i]))
#     print("-" * 30)
#
# def get_stats(records):
#     if not records:
#         print("还没有记录，无法统计")
#         return
#     total = 0
#     for r in records:
#         parts = r.split(" ")
#         total += int(parts[1])
#     count = len(records)
#     print("笔数：%d" % count)
#     print("总支出：%d 元" % total)
#     print("平均每笔：%.2f 元" % (total / count))
#
# def main():
#     records = []
#     while True:
#         print()
#         print("===== 记账本 =====")
#         print("1. 添加记录")
#         print("2. 查看全部")
#         print("3. 统计")
#         print("4. 退出")
#         choice = input("请选择：").strip()
#         if choice == "1":
#             add_record(records)
#         elif choice == "2":
#             show_all(records)
#         elif choice == "3":
#             get_stats(records)
#         elif choice == "4":
#             print("再见")
#             break
#         else:
#             print("无效选项，请输入 1-4")
#
# main()
#
# 讲评（这是今天最值得读的部分）：
#   ① 为什么拆成 4 个函数？
#      因为 main 只负责"调度"，每个功能各管一件事。
#      改统计逻辑只动 get_stats，不会碰到别的。
#   ② 为什么 add_record 返回 True/False？
#      让调用方知道成没成功。真实项目里这个返回值会决定是否提示用户。
#   ③ 为什么先 strip() 再判空？
#      用户输入全是空格时，直接 if not item 判断不出来。
#   ④ 为什么金额用 isdigit() 而不是 try/except？
#      因为异常处理你还没学（第八章）。今天够用，学了再改。
#   ⑤ 统计为什么不单独存金额列表？
#      这里用 "项目 金额" 一个字符串存一条，是为了少用一个数据结构。
#      明天学了字典，更好的做法是 [{"item":"午餐","money":25}, ...]。
#      —— 数据结构选得好，代码短一半。这就是明天字典的意义。
