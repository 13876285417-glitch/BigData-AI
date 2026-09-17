#!/usr/bin/env python3
"""清理 WorkBuddy 预览面板注入到本地 HTML 的 data-page-node-id 属性。

安全性：
- 只删除 ` data-page-node-id="..."` 这一段属性，不改动任何其他内容；
- 清理前后用 html.parser 校验标签结构一致，异常则不写回。
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

PATTERN = re.compile(r'\s+data-page-node-id="[^"]*"')


class TagChecker(HTMLParser):
    """收集标签序列，用于对比清理前后结构是否一致。"""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(("start", tag))

    def handle_endtag(self, tag):
        self.tags.append(("end", tag))

    def handle_startendtag(self, tag, attrs):
        self.tags.append(("startend", tag))


def tag_sequence(text):
    p = TagChecker()
    p.feed(text)
    return p.tags


def main(paths):
    total = 0
    for path in paths:
        p = Path(path)
        original = p.read_text(encoding="utf-8")
        hits = len(PATTERN.findall(original))
        if hits == 0:
            print(f"  -- {p}: 无需清理")
            continue

        cleaned = PATTERN.sub("", original)

        # 结构校验：标签序列必须完全一致
        if tag_sequence(original) != tag_sequence(cleaned):
            print(f"  !! {p}: 标签结构发生变化，已跳过（未写回）")
            continue

        p.write_text(cleaned, encoding="utf-8")
        saved = len(original) - len(cleaned)
        total += hits
        print(f"  OK {p}: 清理 {hits} 处，文件减小 {saved} 字节")

    print(f"\n合计清理 {total} 处注入属性")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("用法: clean_page_node_id.py <file> [file ...]")
        sys.exit(1)
    main(args)
