# 1 * 1 = 1
# 2 * 3 = 6 == 需要两个变量
i = 1
while i <= 9:
    j = 1
    while j <= i:
        # 格式化输出
        print('%d * %d = %d' % (j, i, i*j), end='\t') # 叫做制表符号
        j += 1
    print()
    i += 1
