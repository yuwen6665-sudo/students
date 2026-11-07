# 成绩分级：≥90 优秀 / ≥80 良好 / ≥70 中等 / ≥60 及格 / 其余不及格
grade = int(input("请输入成绩："))
if grade >= 90:
    print("优秀")
elif grade >= 80:
    print("良好")
elif grade >= 70:
    print("中等")
elif grade >= 60:
    print("及格")
else:
    print("不及格")