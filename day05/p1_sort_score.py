# 成绩表排序：给定 
# `[("小明",85),("小红",92),("小刚",78)]`，按分数从高到低打印

scores = [("小明",85),("小红",92),("小刚",78)]
sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
for name, score in sorted_scores:
    print(f"{name}: {score}")