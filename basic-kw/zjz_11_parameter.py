#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author:ZJZ
# datetime:2018/12/22 9:49
# IDE: PyCharm


# ---------------------不可变和可变的参数--------------------
# 无论传递的参数是 可变 还是 不可变
# 只要 针对参数 使用 赋值语句，会在 函数内部 修改 局部变量的引用，不会影响到 外部变量的引用
def demo(num, num_list):
    print("函数内部代码")

    # num = num + num
    num += num
    # num_list.extend(num_list) 由于是调用方法，所以不会修改变量的引用
    # 函数执行结束后，外部数据同样会发生变化
    num_list += num_list

    print(num)
    print(num_list)
    print("函数代码完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)


# ---------------------缺省参数--------------------
# 1. 缺省参数，需要使用 最常见的值 作为默认值！
# 2. 如果一个参数的值 不能确定，则不应该设置默认值，具体的数值在调用函数时，由外界传递！
# 3. 必须保证 带有默认值的缺省参数 在参数列表末尾

# 在 调用函数时，如果有 多个缺省参数，需要指定参数名，这样解释器才能够知道参数的对应关系！
def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s%s 是 %s" % (title, name, gender_text))


# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
print_info("老王", title="班长")
print_info("小美", gender=False)


# ---------------------多值参数--------------------
# 有时可能需要 一个函数 能够处理的参数 个数 是不确定的，这个时候，就可以使用 多值参数
# python 中有 两种 多值参数：
# 1. 参数名前增加 一个 * 可以接收 元组
# 2. 参数名前增加 两个 * 可以接收 字典
#
# 一般在给多值参数命名时，习惯使用以下两个名字
# *args —— 存放 元组 参数，前面有一个 *
# **kwargs —— 存放 字典 参数，前面有两个 *
# args 是 arguments 的缩写，有变量的含义
# kw 是 keyword 的缩写，kwargs 可以记忆 键值对参数

def demo1(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo1(1, 2, 3, 4, 5, name="xm", age=18, gender=True)


# ---------------------元组和字典的拆包--------------------
# 在调用带有多值参数的函数时，如果希望：
# 将一个 元组变量，直接传递给 args
# 将一个 字典变量，直接传递给 kwargs
# 就可以使用 拆包，简化参数的传递，拆包 的方式是：
# 在 元组变量前，增加 一个 *
# 在 字典变量前，增加 两个 *
def demo2(*args, **kwargs):

    print(args)
    print(kwargs)


# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# 会把 num_tuple 和 xiaoming 作为元组传递个 args
# demo(gl_nums, gl_xiaoming)
demo2(*gl_nums, **gl_xiaoming)


# ---------------------函数的递归--------------------
# 函数内部的 代码 是相同的，只是针对 参数 不同，处理的结果不同
# 当 参数满足一个条件 时，函数不再执行
# 这个非常重要，通常被称为递归的出口，否则 会出现死循环！

# 计算 1 + 2 + ... num 的结果
def sum_numbers(num):
    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return 1

    # 假设 sum_numbers 能够完成 num - 1 的累加
    temp = sum_numbers(num - 1)

    # 函数内部的核心算法就是 两个数字的相加
    return num + temp


print(sum_numbers(2))
