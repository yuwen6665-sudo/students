# ============================================================
#  D06 练习 · 文件读写 + 异常处理（4 道）
#  难度：★ 基础 / ★★ 进阶（加速版必做） / ★★★ 挑战
# ------------------------------------------------------------
#  用法：一次一题，做完运行对照验收；做完一题整段 Ctrl + / 注释掉。
#  注意：这几题会在 E:\study\day06\ 下创建 txt / json 文件，正常现象。
# ============================================================


# ============================================================
#  第 1 题 · 写文件 + 读文件　【★】
# ------------------------------------------------------------
#  ① 用 "w" 模式把 3 行内容写进 note.txt
#  ② 用 "a" 模式追加第 4 行
#  ③ 用 for line in f 逐行读出来打印（每行 strip）
#  验收：
#      文件里有 4 行，打印时不带多余空行
#  提示：write 不自动换行，记得写 \n；encoding="utf-8" 必写
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓
# ---- 第 1 题 ----
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

with open("note.txt", "a", encoding="utf-8") as f:
    f.write("第四行\n")

with open("note.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


# ↑↑↑ 第 1 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 1 题 结束", "=" * 46)


# ============================================================
#  第 2 题 · 安全的读文件函数　【★★】
# ------------------------------------------------------------
#  写 read_lines(path)：
#    文件存在 → 返回行列表（每行已 strip，去掉空行）
#    文件不存在 → 返回空列表，不报错
#    用 try/except FileNotFoundError
#  验收：
#      read_lines("note.txt")        → 4 个元素
#      read_lines("没有这个文件.txt")  → []
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓


def read_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = []
            for line in f:
                s = line.strip()
                if s:                # 跳过空行
                    lines.append(s)
            return lines
    except FileNotFoundError:
        return []

print(read_lines("note.txt"))
print(read_lines("没有这个文件.txt"))
#
# 讲评：
#   ① try 包住了整个 with —— 这是标准写法
#   ② return 写在 try 里面：因为文件打开成功后就可以返回了
#   ③ 如果 s 是空字符串（原文件有空白行），if s 会过滤掉 —— 这是个好习惯
#   ④ 只捕 FileNotFoundError，不写裸 except —— 这样其他错误（比如权限问题）还能暴露

# ↑↑↑ 第 2 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 2 题 结束", "=" * 46)


# ============================================================
#  第 3 题 · 用异常改造输入　【★★】
# ------------------------------------------------------------
#  写 get_int(prompt)：
#    反复要求输入，直到用户输入合法整数为止
#    用 try/except ValueError 实现（不要用 isdigit）
#    输入合法就返回这个整数
#  验收：
#      输入 abc → 提示"请输入整数" → 重新输入
#      输入 12  → 返回 12
#  提示：
#      while True:
#          try:
#              return int(input(prompt))
#          except ValueError:
#              print("请输入整数")
#      —— try 里 return 成功后直接退出循环
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入整数")
    

    

# ↑↑↑ 第 3 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 3 题 结束", "=" * 46)


# ============================================================
#  第 4 题 · 记账本持久化（今天的核心）　【★★★】
# ------------------------------------------------------------
#  实现两个函数，把记账本的数据存到 records.json：

#    save_records(records, path="records.json")
#        → 用 json.dump 写入，ensure_ascii=False, indent=2

#    load_records(path="records.json")
#        → 用 json.load 读出；文件不存在或内容损坏时返回 []

#  然后测试：
#    records = [
#        {"item": "午餐", "money": 25},
#        {"item": "晚餐", "money": 40},
#    ]
#    save_records(records)              # 写文件
#    data = load_records()              # 读回来
#    print(data)                        # 应该是原来那两条
#    print(len(data))                   # 2
#    print(load_records("不存在.json"))   # []，不报错

#  验收：打开 records.json 看，中文是正常的（不是 \u4e2d\u6587）
#  提示：
#    import json
#    写：json.dump(records, f, ensure_ascii=False, indent=2)
#    读：records = json.load(f)
#    异常：except (FileNotFoundError, json.JSONDecodeError)
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓

import json


def save_records(records, path="records.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def load_records(path="records.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# 测试
records = [
    {"item": "午餐", "money": 25},
    {"item": "晚餐", "money": 40},
]
save_records(records)
data = load_records()
print(data)
print(len(data))
print(load_records("不存在.json"))
#
# 讲评：
#   ① ensure_ascii=False 是关键：不加的话中文会存成 \u5348\u9910 这种，
#      你能读懂但人看不懂，以后改数据会很痛苦
#   ② indent=2 让 JSON 有缩进、便于人读和手改
#   ③ except 里写了两个异常：
#      FileNotFoundError —— 文件不存在（第一次运行）
#      JSONDecodeError   —— 文件存在但内容坏了（比如你手改错了）
#      —— 两个都要处理，否则坏文件会让程序永远启动不了
#   ④ 为什么用 JSON 不用直接 write 字符串？
#      JSON 把列表+字典的结构原样存下来，读回来还是原结构，
#      不需要你自己设计分隔符、解析格式。这就是「序列化」。
#   ⑤ 这就是今天最有价值的一步：程序有了「状态」。
#      关掉再开数据还在 —— 这一步跨过去，你的程序就从"练习"变成"工具"了。


# ↑↑↑ 第 4 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 4 题 结束", "=" * 46)


print()
print("4 题全部完成。第 4 题写完，记账本就有了「关掉再开数据还在」的能力。")


# ============================================================
#                      参 考 答 案
#          （做完了再看。下面是注释，不会执行）
# ============================================================

# ---- 第 1 题 ----
# with open("note.txt", "w", encoding="utf-8") as f:
#     f.write("第一行\n")
#     f.write("第二行\n")
#     f.write("第三行\n")
#
# with open("note.txt", "a", encoding="utf-8") as f:
#     f.write("第四行\n")
#
# with open("note.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())
#
# 讲评：
#   ① 三次都用 with —— 每次退出代码块文件自动关
#   ② "w" 那次会清空文件，所以必须第一个执行
#   ③ 读的时候 for line in f 比 readlines 省内存
#   ④ strip() 去掉行尾 \n，否则 print 会多空一行

# ---- 第 2 题 ----
# def read_lines(path):
#     try:
#         with open(path, "r", encoding="utf-8") as f:
#             lines = []
#             for line in f:
#                 s = line.strip()
#                 if s:                # 跳过空行
#                     lines.append(s)
#             return lines
#     except FileNotFoundError:
#         return []
#
# print(read_lines("note.txt"))
# print(read_lines("没有这个文件.txt"))
#
# 讲评：
#   ① try 包住了整个 with —— 这是标准写法
#   ② return 写在 try 里面：因为文件打开成功后就可以返回了
#   ③ 如果 s 是空字符串（原文件有空白行），if s 会过滤掉 —— 这是个好习惯
#   ④ 只捕 FileNotFoundError，不写裸 except —— 这样其他错误（比如权限问题）还能暴露

# ---- 第 3 题 ----
# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("请输入整数")
#
# age = get_int("请输入年龄：")
# print("年龄是", age)
#
# 讲评：
#   ① try 里 return 成功后直接退出函数，while 循环自然结束
#   ② except 在下面接住 ValueError，打印提示后循环继续
#   ③ 这个模式叫「重试循环」，真实项目里极其常见
#      —— 比如调 API 失败重试、读配置失败重读，都是这个结构
#   ④ 对比昨天的 isdigit() 方案：try/except 更严谨，
#      isdigit() 只认纯数字，输入 "-5" 会被拒绝（负数也是合法整数）
#      —— 这就是从 isdigit 升级到 try/except 的意义

# ---- 第 4 题 ----
# import json
#
#
# def save_records(records, path="records.json"):
#     with open(path, "w", encoding="utf-8") as f:
#         json.dump(records, f, ensure_ascii=False, indent=2)
#
#
# def load_records(path="records.json"):
#     try:
#         with open(path, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []
#
#
# # 测试
# records = [
#     {"item": "午餐", "money": 25},
#     {"item": "晚餐", "money": 40},
# ]
# save_records(records)
# data = load_records()
# print(data)
# print(len(data))
# print(load_records("不存在.json"))
#
# 讲评：
#   ① ensure_ascii=False 是关键：不加的话中文会存成 \u5348\u9910 这种，
#      你能读懂但人看不懂，以后改数据会很痛苦
#   ② indent=2 让 JSON 有缩进、便于人读和手改
#   ③ except 里写了两个异常：
#      FileNotFoundError —— 文件不存在（第一次运行）
#      JSONDecodeError   —— 文件存在但内容坏了（比如你手改错了）
#      —— 两个都要处理，否则坏文件会让程序永远启动不了
#   ④ 为什么用 JSON 不用直接 write 字符串？
#      JSON 把列表+字典的结构原样存下来，读回来还是原结构，
#      不需要你自己设计分隔符、解析格式。这就是「序列化」。
#   ⑤ 这就是今天最有价值的一步：程序有了「状态」。
#      关掉再开数据还在 —— 这一步跨过去，你的程序就从"练习"变成"工具"了。
