# 输入三个整数，输出其中最大的那个
A = int(input("请输入第一个整数："))
B = int(input("请输入第二个整数："))
C = int(input("请输入第三个整数："))
if A > B and A > C:
    print("最大值是：", A)
elif B > A and B > C:
    print("最大值是：", B)
else:
    print("最大值是：", C)