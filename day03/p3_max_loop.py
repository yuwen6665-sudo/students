max_num = None
while True:
    n = int(input("请输入整数（-1 结束）："))
    if n == -1:
        break
    if max_num is None or n > max_num:
        max_num = n
    print(max_num)