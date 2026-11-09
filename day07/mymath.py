# 里面写 3 个函数：add_data / average / find_max
# 里加 if __name__ == "__main__": 做自测

def add_data(data):
    if not data:
        return 0
    zong = 0
    for num in data:
        zong +=num
    return zong

def average(data):
    return add_data(data)/len(data)

def find_max(data):
    if not data:
        return None
    data_max = data[0]
    for num in data:
        if data_max <num:
            data_max = num
    return  data_max


if __name__ == "__main__":
    print("自测 add_data  :", add_data([1, 2, 3]))      # 6
    print("自测 average   :", average([1, 2, 3]))        # 2.0
    print("自测 find_max  :", find_max([1, 3, 2]))       # 3