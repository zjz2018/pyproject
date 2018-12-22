#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字典同样可以用来 存储多个数据
# 通常用于存储 描述一个 物体 的相关信息
# 和列表的区别
# 列表 是 有序 的对象集合
# 字典 是 无序 的对象集合
# 字典用 {} 定义
# 字典使用 键值对 存储数据，键值对之间使用 , 分隔
# 键 key 是索引
# 值 value 是数据
# 键 和 值 之间使用 : 分隔
# 键必须是唯一的
# 值 可以取任何数据类型，但 键 只能使用 字符串、数字或 元组
# 字典是一个无序的数据集合，使用print函数输出字典时，通常
# 输出的顺序和定义的顺序是不一致的！


xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75,
            "weight": 75.5}

print(xiaoming)


# -------------------基本使用----------------------
xiaoming_dict = {"name": "小明"}

# 1. 取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的key不存在，程序会报错！
# print(xiaoming_dict["name123"])

# 2. 增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"

# 3. 删除
xiaoming_dict.pop("name")
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
# xiaoming_dict.pop("name123")

xiaoming_dict = {"name": "小明",
                 "age": 18}

# 1. 统计键值对数量
print(len(xiaoming_dict))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}

# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)

# 3. 清空字典
xiaoming_dict.clear()

print(xiaoming_dict)


# ---------------------遍历--------------------
xiaoming_dict = {"name": "小明",
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:

    print("%s - %s" % (k, xiaoming_dict[k]))


# ---------------------应用场景--------------------
# 使用 多个键值对，存储 描述一个 物体 的相关信息 —— 描述更复杂的数据信息
# 将 多个字典 放在 一个列表 中，再进行遍历
card_list = [
    {"name": "张三",
     "age": 18,
     "height": 1.75},
    {"name": "李四",
     "age": 20,
     "height": 188}
]

for card_info in card_list:
    print(card_info)
