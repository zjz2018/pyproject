#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("begin")


def sum_2_num(num1, num2):  # num1,num2形参
    """求和

    :param num1: 参数1
    :param num2: 参数2
    :return: 和
    """
    # 函数定义，使用ctrl+q查看，函数前空两行
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))
    return result


res = sum_2_num(11, 19)  # 实参


print("end")
