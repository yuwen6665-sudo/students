# 预设用户名 admin、密码 123456。输出三种结果：
# 登录成功 / 用户名错误 / 密码错误
username = "admin"
password = "123456"
input_username = input("请输入用户名：")
input_password = input("请输入密码：")
if input_username == username and input_password == password:
    print("登录成功")
elif input_username != username:
    print("用户名错误")
else:
    print("密码错误")