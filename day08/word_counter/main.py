"""词频统计器主流程：读文件 → 清洗 → 统计 → 打印报告"""

from pathlib import Path

import counter

BASE_DIR = Path(__file__).resolve().parent


def main(path=None, top=10):
    # 默认读脚本同目录的 sample.txt，不受"从哪个目录启动"影响
    path = BASE_DIR / "sample.txt" if path is None else Path(path)

    text = counter.read_text(path)
    if text is None:
        return

    words = counter.clean_words(text)
    counts = counter.count_words(words)
    ranking = counter.top_n(counts, top)

    print("=" * 42)
    print("文件：%s" % path.name)
    print("总词数：%d" % len(words))
    print("不同词：%d" % len(counts))
    print("=" * 42)

    if not ranking:
        print("没有可统计的词")
        return

    print("前 %d 名（次数降序，同次数按字母序）：" % len(ranking))
    for i, (word, times) in enumerate(ranking, start=1):
        print("%2d. %-15s %3d 次" % (i, word, times))


if __name__ == "__main__":
    main()
