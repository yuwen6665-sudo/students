
def zhishu(num):
    if num < 2:
        return False
    for i in range(2,int(num*0.5)+1):
        if num%i ==0:
            return False
    return True
while True:
    num = int(input("请输入一个整数："))
    if zhishu(num):
        print(num,"是质数")
    else:
        print(num,"不是质数")