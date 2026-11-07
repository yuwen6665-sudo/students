
n=int(input("请输入 n："))
for i in range(1,n+1):
    kong=n-i
    for k in range(1,kong+1):
        print("    ",end="")
    for j in range(1,2*i):
        print("*",end="   ")
    print()