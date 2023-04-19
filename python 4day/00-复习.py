# 循环  和 字符串（下标和切片）
# 循环： while 和 for -- 控制命令重复执行

'''
i = 0  初始值
while 条件:
    命令
    i += 1 循环增量
'''
'''
for 临时变量 in 序列名:
    命令
'''
# i = 0
# while i < 5:
#     print('ok')
#     j = 0
#     while j < 3:
#         print('j')
#         j += 1
#
#     i += 1


str1 = 'hello'
# str1[0]
# print(str1[1:5:-1])
# print(str1[::-1])



# for i in str1:
#     print(i)

i = 0
while i < 4:
    # print(i)

    i += 1
    if str1[i] == 'l':
        continue
    print(str1[i])
# 先判断再执行





