'''
可变数据类型：通过程序改变数据的时候，如果可以改变原有的变量所存储的数据
    列表，字典
不可变数据类型：通过程序改变数据的时候，如果不能改变原有的变量所存储的数据，
    字符串，元组，整型，浮点型
'''


mystr = ' Python hello world ni hao Python '

# ***** mystr.replace(旧的子串，新子串，替换的次数) # 注意：次数不能超过这个子串出现的次数
# print(mystr.replace('python', 'abc', 1))
# print(mystr)  # 验证字符串是不可变数据类型

# ****  strip():去掉收尾的空格，lstrip() -- 左边的空格和rstrip() -- 右边的空格
# print(mystr)
# print(mystr.strip())


# ***********    split(分割符号)：把字符串分割成列表
# print(mystr.strip().split(' '))

# ****大写
# print(mystr.upper())

# *****小写
# print(mystr.lower())

# 单词首字母大写
# print(mystr.title())

# 字符串首字母大写，其余都小写
# print(mystr.strip().capitalize())

# 大小写互转
# print(mystr.swapcase())


# 了解  在某个距离内居中；100指的是100个字符的宽度距离
print(mystr.center(100))
