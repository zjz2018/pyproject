#!/usr/bin/env python3
# -*- coding: utf-8 -*-

row = 1
while row <= 9:
    col = 1
    while col <= row:
        # print("*", end="")  # 同行显示
        print("%d * %d = %d" % (col, row, col * row), end="\t")  # \t制表符，垂直对齐
        col += 1  # 赋值运算 ==，+=，-=
    print("")  # 换行
    row += 1  # 计数器迭代
