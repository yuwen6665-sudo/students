# 词频统计器

读一个文本文件，清洗成词，统计出现次数，输出前 N 名。

## 运行

    python main.py

默认读同目录的 `sample.txt`，输出前 10 名。

读别的文件：

    python main.py other.txt

## 文件

| 文件 | 职责 |
|---|---|
| `main.py` | 主流程：读文件、调函数、打印报告 |
| `counter.py` | 四个函数：`read_text` / `clean_words` / `count_words` / `top_n` |
| `sample.txt` | 测试文本，约 150 词 |

## 处理流程

    read_text(sample.txt)        → 整个文件的字符串
        ↓ clean_words
    ['python', 'is', 'a', ...]   → 转小写、标点变空格、切词
        ↓ count_words
    {'python': 20, 'code': 15}   → 每个词的次数
        ↓ top_n
    [('python', 20), ...]        → 次数降序，取前 N

## 单独测 counter.py

    python counter.py

读同目录的 `sample.txt`，打印总词数和前 5 名。用 `__file__` 定位路径，换目录运行也能找到文件。

## 已知局限

- 没过滤停用词，`the` / `a` / `is` 这类功能词会占榜单前排。真实词频统计通常先去掉 stop words
- 连字符词（`well-known`）会被切成两个词
- 英文缩写（`it's`）会被切成 `it` 和 `s`
