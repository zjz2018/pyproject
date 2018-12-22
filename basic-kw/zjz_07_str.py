#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ---------------------定义--------------------
# 虽然可以使用 \" 或者 \' 做字符串的转义，但是在实际开发中：
# 如果字符串内部需要使用 "，可以使用 ' 定义字符串
# 如果字符串内部需要使用 '，可以使用 " 定义字符串
str1 = "hello python"

str2 = '我的外号是"大西瓜"'

print(str2)
print(str1[6])

for char in str2:

    print(char)


# ---------------------统计--------------------
hello_str = "hello hello"

# 1. 统计字符串长度
print(len(hello_str))

# 2. 统计某一个小（子）字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("abc"))

# 3. 某一个子字符串出现的位置
print(hello_str.index("llo"))
# 注意：如果使用index方法传递的子字符串不存在，程序会报错！
print(hello_str.index("abc"))


# ---------------------判断--------------------
# 1. 判断空白字符
space_str = "      \t\n\r"

print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
# 1> 都不能判断小数
# num_str = "1.1"
# 2> unicode 字符串
# num_str = "\u00b2"
# 3> 中文数字
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())


# ---------------------查找和替换--------------------
hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("Hello"))

# 2. 判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3. 查找指定字符串
# index同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))
# index如果指定的字符串不存在，会报错
# find如果指定的字符串不存在，会返回-1
print(hello_str.find("abc"))

# 4. 替换字符串
# replace方法执行完成之后，会返回一个新的字符串
# 注意：不会修改原有字符串的内容
print(hello_str.replace("world", "python"))

print(hello_str)


# ---------------------文本对齐--------------------
# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对齐输出以下内容
poem = ["\t\n登鹳雀楼",
         "王之涣",
         "白日依山尽\t\n",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]

for poem_str in poem:

    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10, "　"))


# ---------------------拆分拼接--------------------
# 假设：以下内容是从网络上抓取的
# 要求：
# 1. 将字符串中的空白字符全部去掉
# 2. 再使用 " " 作为分隔符，拼接成一个整齐的字符串
poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\t\n更上一层楼"

print(poem_str)

# 1. 拆分字符串 str 默认包含 '\r', '\t', '\n' 和空格
poem_list = poem_str.split()
print(poem_list)

# 2. 合并字符串
result = " ".join(poem_list)
print(result)


# ---------------------切片--------------------
# 字符串[开始索引:结束索引:步长]
# 指定的区间属于 左闭右开 型 [开始索引, 结束索引) => 开始索引 >= 范围 < 结束索引
# 从 起始 位开始，到 结束位的前一位 结束（不包含结束位本身)
# 从头开始，开始索引 数字可以省略，冒号不能省略
# 到末尾结束，结束索引 数字可以省略，冒号不能省略
# 步长默认为 1，如果连续切片，数字和冒号都可以省略
num_str = "0123456789"

# 截取从2 ~ 5的字符串
num_str[2:6]
# 截取从2 ~ 末尾的字符串
num_str[2:]
# 截取从开始 ~ 5的字符串
num_str[:6]
# 截取完整的字符串
num_str[:]
# 从开始位置，每隔一个字符截取字符串
num_str[::2]
# 从索引1开始，每隔1个取一个
num_str[1::2]
# 截取2 ~ 末尾-1 的字符串
num_str[2:-1]
# 截取字符串末尾两个字符
num_str[-2:]
# 字符串的逆序
num_str[::-1]