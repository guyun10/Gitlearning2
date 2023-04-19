# result = 0
# i = 1
# # 1+ 2  + 3 +4 ....
# while i <= 100:
#     # 加法
#     result = result + i
#     # result = 0 + 1
#     # result = 1 + 1
#     i += 1
#     # print(result)  -- 加一次就打印一次
# print(result)

# 偶数和
# 结果
# i 数值
# result = 0
# i = 0
# while i <= 100:
#     result += i
#     i +=2
# print(result)

# 偶数是能被2整除的 -- 取余数是0
result = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(result)

