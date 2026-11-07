#   输入一个整数，输出它是「正偶数 / 正奇数 /
# 负偶数 / 负奇数」之一（0 单独输出「零」）
n = int(input("请输入一个整数"))
if n>0:
    if n%2==0:
        print("这个数是正偶数")
    else:
        print("这个数是正奇数")
elif n<0:
    if n%2==0:
        print("这个数是负偶数")
    else:
        print("这个数是负奇数")
else:
    print("这个数是零")