import tools
import storage


def main():
    records = storage.load_records()
    while True:
        print("\n===== 记账本 v4 =====")
        print("1. 添加  2. 查看  3. 删除  4. 筛选  5. 排序  6. 统计  0. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            item = input("项目：").strip()
            raw = input("金额：").strip()
            if tools.add(records, item, raw):
                storage.save_records(records)
        elif choice == "2":
            tools.show_all(records)
        elif choice == "3":
            tools.show_all(records)
            idx = input("删第几条：").strip()
            if idx.isdigit() and tools.remove_by_index(records, int(idx)):
                storage.save_records(records)
        elif choice == "4":
            kw = input("关键词：").strip()
            tools.show_list(tools.filter_by_item(records, kw))
        elif choice == "5":
            way = input("1. 从大到小  2. 从小到大：").strip()
            if way in ("1", "2"):
                tools.sort_by_money(records, desc=(way == "1"))
                tools.show_all(records)
            else:
                print("请输入 1 或 2")
        elif choice == "6":
            tools.get_stats(records)
        elif choice == "0":
            print("再见")
            break
        else:
            print("无效选项，请输入 0-6")


if __name__ == "__main__":
    main()
