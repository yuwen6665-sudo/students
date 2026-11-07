# ============================================================
#  D05 练习 · 容器收尾 + 函数进阶（4 道）
#  难度：★ 基础 / ★★ 进阶（加速版必做） / ★★★ 挑战
# ------------------------------------------------------------
#  用法：一次一题，做完运行对照验收；做完一题整段 Ctrl + / 注释掉。
#  硬要求：每题造 3 组边界输入（空、单元素、重复）
# ============================================================


# ============================================================
#  第 1 题 · 按分数排序　【★★】
# ------------------------------------------------------------
#  students = [("小明", 85), ("小红", 92), ("小刚", 78), ("小美", 92)]
#  ① 按分数从高到低打印（分数相同按名字升序）
#  ② 打印平均分（保留 2 位）
#  ③ 打印最高分的人名（如果并列，全打印出来）
#  验收：
#      排序：小红 92 / 小美 92 / 小明 85 / 小刚 78
#      平均分：86.75
#      最高分：小红、小美
#  提示：
#      students.sort(key=lambda s: (-s[1], s[0]))
#      最高分的人：先求 max 分数，再筛选出等于它的
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓

students = [("小明", 85), ("小红", 92), ("小刚", 78), ("小美", 92)]

# ① 分数降序、同分名字升序
students.sort(key=lambda s: (-s[1], s[0]))
for name, score in students:
    print("%s %d" % (name, score))

# ② 平均分
total = 0
for name, score in students:
    total += score
print("平均分：%.2f" % (total / len(students)))

# ③ 最高分，并列全打印
top = max(s[1] for s in students)
names = [name for name, score in students if score == top]
print("最高分：%s" % "、".join(names))


# ↑↑↑ 第 1 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 1 题 结束", "=" * 46)


# ============================================================
#  第 2 题 · 去重并保持顺序　【★★】
# ------------------------------------------------------------
#  nums = [3, 1, 3, 2, 1, 4, 2, 5]
#  要求：去重后输出 [3, 1, 2, 4, 5]，**顺序必须和第一次出现一致**
#  禁止：不能直接用 list(set(nums))（会打乱顺序）
#  验收：输出 [3, 1, 2, 4, 5]
#  提示：建一个空列表，遍历原列表，not in 才 append
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓
nums = [3, 1, 3, 2, 1, 4, 2, 5]
lst=[]
for num in nums:
    if num not in lst:
        lst.append(num)
print(nums)
print(lst)

# ↑↑↑ 第 2 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 2 题 结束", "=" * 46)


# ============================================================
#  第 3 题 · 字典合并（同键取高分）　【★★】
# ------------------------------------------------------------
#  a = {"语文": 85, "数学": 90}
#  b = {"英语": 78, "数学": 95}
#  合并成一个新字典，同名的键取较高分
#  验收：{"语文": 85, "数学": 95, "英语": 78}
#  提示：先 dict(a) 复制一份，再遍历 b，用 get 比较
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓

a = {"语文": 85, "数学": 90}
b = {"英语": 78, "数学": 95}

result = dict(a)                 # ① 复制一份,不改原字典
for k, v in b.items():           # ② 遍历 b 的每个键值对
    if k in result:              # ③ 键已存在 → 取较高分
        result[k] = max(result[k], v)
    else:                        # ④ 新键 → 直接加入
        result[k] = v

print(result)                    # {'语文': 85, '数学': 95, '英语': 78}



# ↑↑↑ 第 3 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 3 题 结束", "=" * 46)


# ============================================================
#  第 4 题 · 综合：把记账本能用的工具函数写出来　【★★★】
# ------------------------------------------------------------
#  用字典存记录：{"item": "午餐", "money": 25}
#  写 5 个工具函数（先不管菜单，只写函数并单独测试）：
#
#    add(records, item, money)           → 添加，成功返回 True
#    remove_by_index(records, idx)       → 按序号删（序号从 1 开始），越界返回 False
#    filter_by_item(records, keyword)    → 返回项目名包含关键词的记录列表
#    sort_by_money(records, reverse)     → 按金额排序（用 in 判断 reverse）
#    get_stats(records)                  → 返回 (总支出, 平均, 笔数)，空列表返回 (0,0,0)
#
#  验收（写在代码里自己测）：
#    records = []
#    add(records, "午餐", 25)      → True
#    add(records, "晚餐", 40)      → True
#    add(records, "交通", 5)       → True
#    remove_by_index(records, 2)   → True，剩午餐和交通
#    filter_by_item(records, "餐") → 只剩午餐（因为晚餐被删了）
#    sort_by_money(records)        → 交通 5 在前，午餐 25 在后
#    get_stats(records)            → (30, 15.0, 2)
#  提示：这些函数就是记账本 v3 的核心，写完明天直接用
# ============================================================

↓↓↓ 在这里写你的代码 ↓↓↓
def add(records, item, money):
    if not item or money <= 0:
        return False
    records.append({"item": item, "money": money})
    return True


def remove_by_index(records, idx):
    if idx < 1 or idx > len(records):
        return False
    records.pop(idx - 1)          # 序号从 1 开始，索引从 0 开始
    return True


def filter_by_item(records, keyword):
    result = []
    for r in records:
        if keyword in r["item"]:   # 字符串包含判断用 in
            result.append(r)
    return result


def sort_by_money(records, reverse=False):
    records.sort(key=lambda r: r["money"], reverse=reverse)
    return records


def get_stats(records):
    if not records:
        return 0, 0, 0
    total = 0
    for r in records:
        total += r["money"]
    count = len(records)
    return total, round(total / count, 2), count


# ---- 自测 ----
records = []
print(add(records, "午餐", 25))        # True
print(add(records, "晚餐", 40))        # True
print(add(records, "交通", 5))         # True
print(remove_by_index(records, 2))     # True
print(records)                          # [{'item':'午餐','money':25}, {'item':'交通','money':5}]
print(filter_by_item(records, "餐"))   # [{'item':'午餐','money':25}]
sort_by_money(records)
print(records)                          # 交通在前，午餐在后
print(get_stats(records))               # (30, 15.0, 2)


# ↑↑↑ 第 4 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 4 题 结束", "=" * 46)


print()
print("4 题全部完成。第 4 题写完，明天记账本 v3 只需要接菜单。")


# ============================================================
#                      参 考 答 案
#          （做完了再看。下面是注释，不会执行）
# ============================================================

# ---- 第 1 题 ----
# students = [("小明", 85), ("小红", 92), ("小刚", 78), ("小美", 92)]
#
# # ① 排序：分数降序、同分按名字升序
# students.sort(key=lambda s: (-s[1], s[0]))
# for name, score in students:
#     print(name, score)
#
# # ② 平均分
# total = 0
# for _, score in students:
#     total += score
# print("平均分：%.2f" % (total / len(students)))
#
# # ③ 最高分的人
# top = max(s[1] for s in students)
# names = [s[0] for s in students if s[1] == top]
# print("最高分：", "、".join(names))
#
# 讲评：
#   ① key=lambda s: (-s[1], s[0]) 是「多级排序」：
#      先按 -分数（降序），分数相同再按名字（升序）。
#      返回一个元组，Python 会按元组顺序依次比较。
#   ② for _, score in students —— 用下划线 _ 表示"这个值我不要"，
#      这是 Python 的惯例，面试官看你这么写会觉得你专业。
#   ③ max(s[1] for s in students) 是「生成器表达式」，
#      比 [s[1] for s in students] 省内存。现在会写就行。

# ---- 第 2 题 ----
# nums = [3, 1, 3, 2, 1, 4, 2, 5]
# result = []
# for n in nums:
#     if n not in result:
#         result.append(n)
# print(result)      # [3, 1, 2, 4, 5]
#
# 讲评：
#   ① 为什么不能 list(set(nums))？因为集合无序，结果是 [1,2,3,4,5]，
#      顺序全乱了。
#   ② 这个方法的时间复杂度是 O(n²)（每个元素都要扫一遍 result）。
#      数据量小时无所谓，大时要改用字典保序的写法：
#        seen = {}; result = []
#        for n in nums:
#            if n not in seen:
#                seen[n] = True
#                result.append(n)
#      字典查键是 O(1)，整体变 O(n)。这就是"数据结构选对，代码快一个量级"。
#   ③ Python 3.7+ 的 dict 保插入顺序，`list(dict.fromkeys(nums))` 也能一行去重，
#      但那个你现在不用记。

# ---- 第 3 题 ----
# a = {"语文": 85, "数学": 90}
# b = {"英语": 78, "数学": 95}
#
# merged = dict(a)                 # 先复制 a
# for k, v in b.items():
#     if k in merged and merged[k] > v:
#         continue                 # a 里已有更高分，保留
#     merged[k] = v                # 否则写入 b 的值
#
# print(merged)    # {'语文': 85, '数学': 95, '英语': 78}
#
# 讲评：
#   ① dict(a) 才是复制！直接 merged = a 会改到原来的 a（还记得 B4 那个坑吗）
#   ② 等价简写：merged[k] = max(merged.get(k, 0), v)
#      这一行就搞定，但可读性不如上面清楚 —— 面试时写清楚比写短重要。

# ---- 第 4 题 ----
# def add(records, item, money):
#     if not item or money <= 0:
#         return False
#     records.append({"item": item, "money": money})
#     return True
#
#
# def remove_by_index(records, idx):
#     if idx < 1 or idx > len(records):
#         return False
#     records.pop(idx - 1)          # 序号从 1 开始，索引从 0 开始
#     return True
#
#
# def filter_by_item(records, keyword):
#     result = []
#     for r in records:
#         if keyword in r["item"]:   # 字符串包含判断用 in
#             result.append(r)
#     return result
#
#
# def sort_by_money(records, reverse=False):
#     records.sort(key=lambda r: r["money"], reverse=reverse)
#     return records
#
#
# def get_stats(records):
#     if not records:
#         return 0, 0, 0
#     total = 0
#     for r in records:
#         total += r["money"]
#     count = len(records)
#     return total, round(total / count, 2), count
#
#
# # ---- 自测 ----
# records = []
# print(add(records, "午餐", 25))        # True
# print(add(records, "晚餐", 40))        # True
# print(add(records, "交通", 5))         # True
# print(remove_by_index(records, 2))     # True
# print(records)                          # [{'item':'午餐','money':25}, {'item':'交通','money':5}]
# print(filter_by_item(records, "餐"))   # [{'item':'午餐','money':25}]
# sort_by_money(records)
# print(records)                          # 交通在前，午餐在后
# print(get_stats(records))               # (30, 15.0, 2)
#
# 讲评（这是今天最值钱的一段）：
#   ① remove_by_index 里 idx - 1 是「序号→索引」的转换。
#      用户看到的第 1 条，索引是 0。这个转换在真实项目里到处都是（分页、报表）。
#   ② 越界检查 idx < 1 or idx > len(records) —— 这是卫语句，
#      挡住了程序崩溃的可能。
#   ③ sort_by_money 用 reverse=False 当默认值，
#      调用时 sort_by_money(records) 就是升序，sort_by_money(records, True) 是降序。
#   ④ 这五个函数就是「记账本 v3」的全部逻辑。
#      明天你只需要写一个 main() 把它们串起来 —— 菜单、输入、分发。
#      —— 这就是拆函数的价值：功能可测试、可复用、可单独改。
