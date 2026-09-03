"""大数据与人工智能课程 - 第 1 课示例程序
演示：Python 版本信息 + 简单数据分析
"""
import sys


def main():
    print("=" * 50)
    print("大数据与人工智能课程 · 第 1 课")
    print("=" * 50)
    print(f"Python 版本: {sys.version.split()[0]}")

    # 简单示例：列表与求和
    scores = [85, 92, 78, 90, 88]
    total = sum(scores)
    average = total / len(scores)
    print(f"成绩列表: {scores}")
    print(f"总分: {total}，平均分: {average:.1f}")


if __name__ == "__main__":
    main()
