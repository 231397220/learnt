i_luck_num = 46
luck_num = 0

for i in range(3):
    luck_num = int(input("请猜下幸运数字:"))
    if i_luck_num < luck_num:
         print("输入的数字大了")
    elif i_luck_num > luck_num:
        print("输入的数字小了")
    else:
        print("猜对了")
        break

else:
    print("尝试太多次")

