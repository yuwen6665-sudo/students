zifu=input("请输入一个字符串：")
shuzi=0
zimu=0
qita=0
for ch in zifu:
    if ch.isdigit():
        shuzi+=1
    elif ch.isalpha():
        zimu+=1 
    else:
        qita+=1
print(f"数字 {shuzi}、字母 {zimu}、其他 {qita}")