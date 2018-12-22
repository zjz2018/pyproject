#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

player = int(input("1石头，2剪刀，3布 请输入："))
computer = random.randint(1, 3)
# 格式化字符：%s 字符串, %d 整数 --%06d 6位整数，不足0补齐, %f 浮点数 --%.2f保留两位小数, %% 输出%
print("玩家出 %d ,电脑出 %d " % (player, computer))
if ((player == 1 and computer == 2)  # 条件过长，使用括号，然后在逻辑运算符（and or not）换行，并且8个缩进
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家获胜！")
elif player == computer:
    print("平局")
else:
    print("电脑获胜！")
