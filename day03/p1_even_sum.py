n=int(input("请输入 n："))
num=0
for i in range(1,n+1):
    if i%2==0:
       num+=i
print(num)