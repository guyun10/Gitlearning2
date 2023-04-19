# 用户输入1-4的数字，提示数字的意义（1-石头；2-剪刀，3-布，4-退出）
# 玩家输入如果是4，退出
# 如果玩家输入的是1-3，让电脑出拳（不一定 -- 随机数） ，让这两个数做判断： -- if嵌套
    # 判断什么时候自己赢了
    # 平局
    # 电脑获胜
# 如果输入的是1-4以外的 打印输入错了

import random
# 先定义一个开关（变量）默认让用户可以玩游戏，开关默认是打开的；当用户输入4的时候关闭开关（退出循环）
kaiguan = 'yes'
while kaiguan == 'yes':
    c = random.randint(1, 3)
    # print(computer)
    p = int(input('请出拳：1-石头；2-剪刀，3-布，4-退出：'))
    if p == 4:
        print('已经退出')
        # 关闭循环  - 设置开关不为yes
        kaiguan = 'no' # 重新把kaiguan变量赋值
    elif 1 <= p <= 3:
        # if
        # pass 为了语法不报错过，一会填充命令
        if (p == 1 and c == 2) or (p == 2 and c == 3) or (p == 3 and c == 1):
            print('玩家获胜')
        elif p == c:
            print('平局')
        else:
            print('电脑获胜')
    else:
        print('请输入有效的数字')



