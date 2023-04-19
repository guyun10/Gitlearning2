# 正序排列（从小到大），默认的reverse=False
# 从大到小，reverse=True

# sort():python3不支持不同的数据类型排序；python2中支持，ASCII码排序
list1 = [1, 2, 4, 3, 5, 10, 6]
# list1.sort(reverse=True)
# print(list1)


# sorted():不会改变原有的列表，返回一个新的列表
list2 = sorted(list1, reverse=True)
print(list2)

