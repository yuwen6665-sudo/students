# 分段计费：用电 0–180 度 0.6 元/度
# ；181–350 度超出部分 1.0 元/度；>350 度超出部分 1.5 元/度
yongdian = int(input("请输入用电量："))
if yongdian <= 180:
    feiyong = yongdian * 0.6
elif yongdian <= 350:
    feiyong = 180 * 0.6 + (yongdian - 180) * 1.0
else:
    feiyong = 180 * 0.6 + (350 - 180) * 1.0 + (yongdian - 350) * 1.5
print("电费为：%.2f元"%feiyong)