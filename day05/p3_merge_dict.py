# 字典合并与统计：两个字典
# {"语文":85,"数学":90} 和 {"英语":78,"数学":95} 
# 合并，数学取较高分
dict_a = {"语文":85,"数学":90}
dict_b = {"英语":78,"数学":95}
merged_dict = dict_a.copy()
for subject, score in dict_b.items():
    if subject in merged_dict:
        merged_dict[subject] = max(merged_dict[subject], score)
    else:
        merged_dict[subject] = score
print(merged_dict)