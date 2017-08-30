i_luck_num = 46
luck_num = 0
limit_num = 0

while limit_num < 3: #i_luck_num != luck_num and
    luck_num = int(input("请猜下幸运数字:"))


    if i_luck_num < luck_num:
         print("输入的数字大了")
    elif i_luck_num > luck_num:
        print("输入的数字小了")
    else:
        print("猜对了")
        break
#    limit_num = limit_num + 1
    limit_num += 1

else:
    print("尝试太多次")

# if i_luck_num == limit_num:
#     print("你猜对了")
# else:
#     print("尝试太多次")