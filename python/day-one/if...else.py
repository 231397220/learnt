#!/usr/bin/evn python3
sex = input("input your gender:")
if sex == "girl":
    print("i woule like to have a little monkey")
elif sex == "man":
    print("going to homesexaul")
else:
    print("pervert")


#猜luckky number,
#猜的数字比你的大,提示说你输入的大,如果小就输入的小了.

i_luck_num = 46
luck_num = int(input("请猜下幸运数字:"))
if i_luck_num < luck_num:
    print("输入的数字大了")
elif i_luck_num > luck_num:
    print("输入的数字小了")
else:
    print("你猜对了")