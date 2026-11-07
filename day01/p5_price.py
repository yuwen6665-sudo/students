# 加餐：单价×数量算总价（保留两位）；身高体重算 BMI
danjia =float(input("请输入单价："))
shuliang =int(input("请输入数量："))
zongjia = danjia * shuliang
print("总价为%f"%zongjia)
hight= float(input("请输入身高："))
weight= float(input("请输入体重："))
bmi = weight / (hight ** 2)
print("你的BMI是%.2f"%bmi)