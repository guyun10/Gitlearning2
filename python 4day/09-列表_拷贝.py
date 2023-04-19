list1 = [1, 2, 3]

# list1 = [1, 2, 3]
# 浅拷贝（一改都改） 和  深拷贝
# list2 = list1
# print(list1)
# print(list2)
# list1[0] = 10
# print(list1)
# print(list2)
# list2[2] = 30
# print(list1)
# print(list2)

list2 = list1.copy()
print(list1)
print(list2)
list1[0] = 100
print(list1)
print(list2)
