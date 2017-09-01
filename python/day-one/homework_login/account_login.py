#!/usr/bin/evn python3


num = 0                                                 #设定一个数值,只允许执行3次使用
while num < 3:                                          #只允许执行3次,执行3次什么内容呢?就在下面
    user_name = input("请输入用户名:")
    user_pass = input("请输入密码:")                      #输入用户名密码


    black_list = open("black.txt","r")                  #打开黑名单
    for black_name in black_list.readlines():           #遍历黑名单中的用户
        # print(black_name.strip('\n'))
        if black_name.strip('\n') == user_name:          #如果用户在黑名单,执行下方操作
            print("%s账户以禁用" %(user_name))
            black_list.close()
            exit()                                       #退出进程
    black_list.close()                                   #没有遍历到时,关闭黑名单



    passwd1 = open('user_passwd1.txt','r')               #打开用户认证库
    for passwd_list in passwd1.readlines():              #遍历所有用户
        (name,password) = passwd_list.strip('\n').split()         #将所有用户名和密码赋值给变量
        # print(passwd_list)
        # print(name)
        # print(password)
        if name == user_name:                           #如果用户名相等,执行下方操作
            if password == user_pass:                   #如果密码相等,执行下方操作
                print("登入成功")
                exit()                                 #显示成功,并退出进程
            elif password != user_pass:                #如果密码不相等,执行下方操作
                num += 1                               #允许执行数量加1
                error_count = open("%s_passws_error.txt" %(user_name),"a")    #打开密码错误次数库
                error_count.write("1")                                         #记录一次密码错误
                error_count.close()                                            #关闭

                print("输入密码错误第%s次,请重新输入密码.\n第三次后账户将会被锁定" %(num))   #输出提示内容
                error_counted = open("%s_passws_error.txt" %(user_name),'r')         #打开密码错误次数库
                error_num = error_counted.read().count("1")                          #统计密码错误次数,并复制给变量
                error_counted.close()                                                #关闭
                # print(error_num)
                if 2 < error_num:                                                    #如果错误次数大于2,执行下方操作
                    print("密码尝试次数过多,账户已被锁定.")                              #打印提示内容
                    black_list = open("black.txt", "a")                              #打开黑名单
                    black_list.write("%s\n" %(user_name))                            #向黑名单中写入,用户名
                    black_list.close()
                    exit()                                                           #退出进程
                break                                                                #如果次数小于3,退出循环

            # print(user_name,name)
            # print("用户存在")


    print("用户不存在")                    #在整个遍历中,如果用户名不相等,打印提示
    break
    passwd1.close()
exit()
