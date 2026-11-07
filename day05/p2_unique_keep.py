列表去重并保持顺序：[3,1,3,2,1,4] → [3,1,2,4]
lest = [3, 1, 3, 2, 1, 4]
unique_list = []
for num in lest:
    if num not in unique_list:
        unique_list.append(num)
print(unique_list)  