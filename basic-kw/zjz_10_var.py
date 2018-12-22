#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author:ZJZ
# datetime:2018/12/21 10:46
# IDE: PyCharm

# 1> 不可变类型，内存中的数据不允许被修改：
# 数字类型 int, bool, float, complex, long(2.x)
# 字符串 str
# 元组 tuple

# 2> 可变类型，内存中的数据可以被修改：
# 列表 list
# 字典 dict
# 注意
#
# 1. 可变类型的数据变化，是通过 方法 来实现的
# 2. 如果给一个可变类型的变量，赋值了一个新的数据，引用会修改
#     变量 不再 对之前的数据引用
#     变量 改为 对新赋值的数据引用
# 3. 字典的 key 只能使用不可变类型的数据


# 全局变量名前应该增加 g_ 或者 gl_ 的前缀
gl_num = 10


def demo1():
    print("demo1" + "-" * 50)

    # global 关键字，告诉 Python 解释器 num 是一个全局变量
    global gl_num
    gl_num = 100
    print(gl_num)


def demo2():
    print("demo2" + "-" * 50)
    print(gl_num)


demo1()
demo2()

print("over")


# 定义函数时，是否接收参数，或者是否返回结果，是根据 实际的功能需求 来决定的！
#
# 1. 如果函数 内部处理的数据不确定，就可以将外界的数据以参数传递到函数内部
# 2. 如果希望一个函数 执行完成后，向外界汇报执行结果，就可以增加函数的返回值


def measure():
    """返回当前的温度"""

    print("开始测量...")
    temp = 39
    wetness = 10
    print("测量结束...")
    # 返回多个值时，使用元组，括号可省略
    return temp, wetness


# 在 Python 中，可以 将一个元组 使用 赋值语句 同时赋值给 多个变量
# 注意：变量的数量需要和元组中的元素数量保持一致
result = temp, wetness = measure()
