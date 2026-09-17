"""
第 1 课作业 · 创建并运行第一个 Python 文件

课程：大数据与人工智能（新闻学方向）
用途：验证 VS Code + Python 环境是否配置成功
运行：在 VS Code 中打开本文件，按下 F5 或点击右上角 ▷ 运行按钮
      也可以先在终端里进入 scripts 目录，再执行 python 01.py
"""

# print() 是 Python 里最基础的"输出"函数
# 括号里的内容会被打印到终端（下方"终端"面板）里
print('我也会写程序啦！')

# —— 下面是自检部分，运行成功后终端会依次打印出环境信息 ——
print('-' * 30)
print('环境自检：')

import sys  # sys 是 Python 自带的标准库，不需要额外安装

print(f'Python 版本：{sys.version.split()[0]}')
print(f'解释器路径：{sys.executable}')
print('-' * 30)
print('环境配置成功，可以开始学习了。')
