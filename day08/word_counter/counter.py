"""词频统计的核心函数：读文本、清洗、计数、排序取前 N"""

import string

# 要替换成空格的标点：ASCII 标点 + 常用中文全角标点
PUNCT = string.punctuation + "，。！？；：“”‘’（）【】《》"
TRANS = str.maketrans({ch: " " for ch in PUNCT})


def read_text(path):
    """读整个文件返回字符串；文件不存在时打印提示并返回 None"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("文件不存在：%s" % path)
        return None


def clean_words(text):
    """转小写 → 标点变空格 → 按任意空白切词，返回词列表"""
    return text.lower().translate(TRANS).split()


def count_words(words):
    """统计每个词出现次数，返回 {词: 次数}"""
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def top_n(count, n=10):
    """按次数降序、同次数按字母升序，返回前 n 个 (词, 次数)"""
    items = sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[:n]


if __name__ == "__main__":
    # 自测：用 __file__ 定位同目录的 sample.txt，换哪个目录运行都能找到
    from pathlib import Path

    sample = Path(__file__).with_name("sample.txt")
    text = read_text(sample)
    if text is not None:
        words = clean_words(text)
        counts = count_words(words)
        print("总词数：%d，不同词：%d" % (len(words), len(counts)))
        print("前 5 名：", top_n(counts, 5))
