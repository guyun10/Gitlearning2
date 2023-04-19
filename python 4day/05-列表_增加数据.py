list1 = ['daqiu', 10, 'erqiu', 20]
# 取数据
# print(list1[0])
# print(list1[0:2])
# for i in list1:
#     print(i)

# 增加
# 参数：小括号写参数，小括号可以书写多个参数，各个参数用逗号隔开
# insert(添加数据的位置下标， 要添加的数据):指定位置添加数据
# list1.insert(2, 'abc')

# append():结尾添加数据：可以是一个，也可以是一个列表
# list1.append('sanqiu')
# list1.append([10, 20, 30])

# extend() : 结尾添加数据，会拆开数据，如果追加的数据是列表的时候常用
# list1.extend('sanqiu')
list1.extend([10, 20, 30])
print(list1)



