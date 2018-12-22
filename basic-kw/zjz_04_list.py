#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 专门用于存储 一串 信息
# 列表用 [] 定义，数据 之间使用 , 分隔
# 列表的 索引 从 0 开始
# 列表 通常存储相同类型的数据
# 通过 迭代遍历，在循环体内部，针对列表中的每一项元素，执行相同的操作


# ------------------基本使用-------------------
name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
# list index out of range - 列表索引超出范围
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_list.index("wangwu"))

# 2. 修改
name_list[1] = "李四"
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错！
# name_list[3] = "王小二"

# 3. 增加
# append 方法可以向列表的末尾追加数据
name_list.append("王小二")
# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(1, "小美眉")

# extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)

# 4. 删除
# remove 方法可以从列表中删除指定的数据
name_list.remove("wangwu")
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
# pop 方法可以指定要删除元素的索引
name_list.pop(3)
# clear 方法可以清空列表
name_list.clear()

print(name_list)


# ----------------删除-----------------------
name_list = ["张三", "李四", "王五"]

# (知道)使用 del 关键字(delete)删除列表元素
# 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]

# del 关键字本质上是用来将一个变量从内存中删除的
name = "小明"

del name

# 注意：如果使用 del 关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了
print(name)

print(name_list)


# ----------------长度-----------------------
name_list = ["张三", "李四", "王五", "王小二", "张三"]

# len(length 长度) 函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了 %d 次" % count)

# 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
name_list.remove("张三")

print(name_list)


# ---------------排序------------------------
name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]

# 升序
# name_list.sort()
# num_list.sort()

# 降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)

# 逆序（反转）
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)


# ----------------遍历-----------------------
name_list = ["张三", "李四", "王五", "王小二"]

# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在　
my_name 这个变量中，在循环体内部可以访问到当前这一次获取到的数据

for my_name in 列表变量:

    print("我的名字叫　%s" % my_name)

"""
for my_name in name_list:

    print("我的名字叫　%s" % my_name)
