#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 用于存储 一串 信息，数据 之间使用 , 分隔
# 元组用 () 定义
# 元组的 索引 从 0 开始
# 作为函数的参数和返回值：一个函数可以接受任意多个参数，或者一次返回多个数据
# 格式字符串：格式化字符串%后面的（）本质就是一个元组
# 让列表不可修改，保护数据
# 在实际开发中，除非 能够确认元组中的数据类型，否则针对元组的循环遍历需求并不是很多


# -------------------基本使用----------------------
info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 1. 取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("zhangsan"))

# 2. 统计计数
print(info_tuple.count("zhangsan"))
# 统计元组中包含元素的个数
print(len(info_tuple))


# ---------------------遍历--------------------
info_tuple = ("zhangsan", 18, 1.75)

# 使用迭代遍历元组
for my_info in info_tuple:

    # 使用格式字符串拼接 my_info 这个变量不方便！
    # 因为元组中通常保存的数据类型是不同的！
    print(my_info)


# ---------------------格式化字符串--------------------
info_tuple = ("小明", 21, 1.85)

# 格式化字符串后面的 `()` 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

# 拼接新字符串
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

print(info_str)


# ---------------------list tuple转化--------------------
name_tuple = ()
# 转化为list 数据可修改
name_list = list(name_tuple)
# 转化为tuple 数据不可修改
tuple(name_tuple)