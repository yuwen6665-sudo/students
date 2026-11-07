# ============================================================
#  D07 练习 · 模块化 + 第三方包（4 道）
#  难度：★ 基础 / ★★ 进阶（加速版必做） / ★★★ 挑战
# ------------------------------------------------------------
#  今天的重点不是写新功能，是「把已有代码拆成能维护的结构」。
#  存放：E:\study\day07\  （每道题建一个子目录）
# ============================================================


# ============================================================
#  第 1 题 · 拆出一个工具模块　【★】
# ------------------------------------------------------------
#  在自己的目录里建两个文件：
#
#    mymath.py      里面写 3 个函数：add_data / average / find_max
#    p1_use_module.py  这个文件 import mymath 并调用三个函数
#
#  要求：
#    mymath.py 里加 if __name__ == "__main__": 做自测
#    p1_use_module.py 里用 import mymath 方式调用
#
#  验收：
#    运行 mymath.py       → 打印自测结果
#    运行 p1_use_module.py → 打印调用结果，且不打印 mymath 的自测
#
#  ↓↓↓ 下面是 p1_use_module.py 的内容（mymath.py 你自己建）↓↓↓
# ============================================================

# import mymath
#
# data = [80, 90, 75]
# print("总和：", mymath.add_data(data))
# print("平均：", mymath.average(data))
# print("最大：", mymath.find_max(data))

# 把上面三行取消注释、建好 mymath.py 之后，运行本文件
print("（第 1 题请在 day07 下建 mymath.py 和 p1_use_module.py 两个文件）")


# ============================================================
#  第 2 题 · 装一个第三方包并用起来　【★】
# ------------------------------------------------------------
#  在终端里执行：pip install requests
#  然后写代码调用它，抓一个公开 API 的数据。
#
#  题目：用 requests 访问 https://api.github.com/users/yuwen6665-sudo
#        打印出 login（用户名）和 public_repos（公开仓库数）
#
#  验收：能打印出你的 GitHub 用户名和仓库数
#
#  提示：
#    import requests
#    r = requests.get("https://api.github.com/users/yuwen6665-sudo")
#    data = r.json()          # 把返回的 JSON 转成字典
#    print(data["login"])
#    print(data["public_repos"])
#
#  注意：这一步你可能遇到网络问题（超时），遇到就记进卡点清单，
#        换成 requests.get 一个国内能访问的地址也行。
# ============================================================

# ↓↓↓ 在这里写你的代码 ↓↓↓



# ↑↑↑ 第 2 题写完到这里 ↑↑↑
print()
print("=" * 46, "第 2 题 结束", "=" * 46)


# ============================================================
#  第 3 题 · 把记账本拆成三个文件　【★★】
# ------------------------------------------------------------
#  这是今天的主任务。目录结构不要用 E:\study\day07\bill_book 之外的路径：
#
#    day07\bill_book\
#      ├── main.py          菜单 + 调度
#      ├── tools.py         add / remove_by_index / filter_by_item
#      │                    / sort_by_money / get_stats
#      ├── storage.py       save_records / load_records（JSON）
#      ├── .gitignore       .venv/ __pycache__/ *.pyc .env records.json
#      └── README.md        项目说明
#
#  实现顺序（不要跳步）：
#    ① 先把昨天能跑的 p1_book_v3.py 复制成 main.py，确认还能跑
#    ② 把 5 个业务函数剪到 tools.py → 改 main.py 加 import → 再跑一次
#    ③ 把 JSON 读写剪到 storage.py → 改 main.py 加 import → 再跑一次
#    ④ 建 .gitignore 和 README.md
#
#  验收：
#    每一步之后程序都能正常跑；最后 main.py 不超过 60 行
#
#  提示：
#    tools.py 里不要 import main
#    main.py 里写：import tools
#                 import storage
#    文件在同一目录，直接 import 文件名（不带 .py）
# ============================================================

# 这一题不需要在这里写代码，在 bill_book 目录下建文件。
# 完成后在这里记一行：
# [ ] 已拆成 3 个文件，每一步都跑通了


# ============================================================
#  第 4 题 · 用异常保护你的程序　【★★★】
# ------------------------------------------------------------
#  在记账本的 storage.py 里，把 load_records 做成"绝不会崩"的版本：
#
#    文件不存在        → 返回 []
#    文件内容不是合法JSON → 返回 []，并打印"数据文件损坏，已重置"
#    文件存在但读不了（权限）→ 返回 []，并打印具体错误
#
#  再在 tools.py 的 add 里加上：
#    金额 <= 0        → 返回 False
#    项目名为空       → 返回 False
#    金额不是数字     → 返回 False（提示调用方）—— 注意这里应该用 try/except
#
#  验收：
#    手动把 records.json 改成一堆乱码 → 程序启动不崩，自动重置
#    手动删掉 records.json         → 程序启动不崩，空列表开始
#
#  提示：
#    except (FileNotFoundError, json.JSONDecodeError):
#    except Exception as e:  # 兜底，打印 e
# ============================================================

# 这一题同样在 bill_book 目录里改，不在这里写。
# 完成后在这里记一行：
# [ ] 乱码文件 / 缺失文件 两种情况下程序都不崩


print()
print("4 题说明已读完。今天的主战场在 day07\\bill_book 目录。")
print("记住纪律：改一处 → 跑一次 → 通过 → 再改下一处。")


# ============================================================
#                    参考答案与要点
#          （做完了再看。下面是注释，不会执行）
# ============================================================

# ---- 第 1 题 ----
# mymath.py:
# def add_data(data):
#     s = 0
#     for n in data:
#         s += n
#     return s
#
# def average(data):
#     if not data:
#         return 0
#     return round(add_data(data) / len(data), 2)
#
# def find_max(data):
#     if not data:
#         return None
#     m = data[0]
#     for n in data:
#         if n > m:
#             m = n
#     return m
#
# if __name__ == "__main__":
#     d = [1, 2, 3]
#     print("自测：", add_data(d), average(d), find_max(d))
#
# 讲评：
#   ① 三个函数都只依赖传进来的 data，不碰全局变量 —— 这叫"纯函数"，好测试
#   ② if __name__ == "__main__" 让这个文件既能被 import，又能单独跑测试
#   ③ p1_use_module.py 用 import mymath 而不是 from mymath import *，
#      这样一眼能看出 add_data 是从 mymath 来的

# ---- 第 2 题 ----
# import requests
#
# url = "https://api.github.com/users/yuwen6665-sudo"
# try:
#     r = requests.get(url, timeout=10)
#     data = r.json()
#     print("用户名：", data["login"])
#     print("公开仓库数：", data["public_repos"])
# except Exception as e:
#     print("请求失败：", e)
#
# 讲评：
#   ① timeout=10 必加 —— 不加的话网络不通会卡死很久
#   ② r.json() 把返回的 JSON 字符串转成 Python 字典
#   ③ 外面套 try/except —— 网络请求是最不可靠的操作，必须防
#   ④ 这一题你第一次用第三方库访问真实互联网。以后调大模型 API 就是这个套路
#      （requests → 拿 JSON → 取字段），只是 URL 和参数不同

# ---- 第 3 题 ----
# 拆分后的 main.py 参考（≤60 行）：
#
# import tools
# import storage
#
#
# def main():
#     records = storage.load_records()
#     while True:
#         print("\n===== 记账本 v4 =====")
#         print("1. 添加  2. 查看  3. 删除  4. 筛选  5. 排序  6. 统计  0. 退出")
#         choice = input("请选择：").strip()
#         if choice == "1":
#             item = input("项目：").strip()
#             raw = input("金额：").strip()
#             if tools.add(records, item, raw):
#                 storage.save_records(records)
#         elif choice == "2":
#             tools.show_all(records)
#         elif choice == "3":
#             idx = input("删第几条：").strip()
#             if idx.isdigit() and tools.remove_by_index(records, int(idx)):
#                 storage.save_records(records)
#         elif choice == "4":
#             kw = input("关键词：").strip()
#             tools.show_list(tools.filter_by_item(records, kw))
#         elif choice == "5":
#             tools.sort_by_money(records)
#             tools.show_all(records)
#         elif choice == "6":
#             tools.get_stats(records)
#         elif choice == "0":
#             storage.save_records(records)
#             break
#         else:
#             print("无效选项")
#
#
# if __name__ == "__main__":
#     main()
#
# 讲评：
#   ① 每次"写操作"（添加/删除）之后立刻 save —— 保证数据不丢
#   ② main 只做调度，没有一句业务逻辑
#   ③ 注意 tools.add 现在接收的是字符串 raw 而不是 int ——
#      把"字符串转数字"的判断放进 tools 里，main 不用管
#      这叫"把校验放到最需要它的地方"

# ---- 第 4 题 ----
# storage.py 的健壮版本：
#
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
#     except FileNotFoundError:
#         return []                     # 第一次运行，正常
#     except json.JSONDecodeError:
#         print("数据文件损坏，已重置")
#         return []
#     except Exception as e:
#         print("读取出错：", e)
#         return []
#
# 讲评（这是今天最有价值的一段）：
#   ① 三种异常分开处理，因为它们代表三种不同情况：
#      - 文件不存在 → 正常的第一次运行，静默返回 []
#      - 文件坏了 → 要提示用户（数据丢了）
#      - 其他错误 → 打印具体信息方便排查
#   ② 如果全用一个 except Exception 打包，你就分不清"第一次运行"和"文件坏了"
#   ③ 最后的 except Exception as e 是兜底，保证函数永远不抛异常
#      —— 这叫"防御性编程"：外部来的东西（文件、网络、用户输入）都不可信
#   ④ 这一题做完，你的程序就有了"工程健壮性"，
#      这正是面试官问"你怎么处理异常"时想听到的东西
