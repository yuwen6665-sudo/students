# **闰年判断**：能被 4 整除且不能被 100 整除，**或者**能被 400 整除
year = int(input("请输入年份："))
if year %4==0 and year%100!=0 or year%400==0:
    print("%d 是闰年" %year)
else:
    print("%d 不是闰年" %year)