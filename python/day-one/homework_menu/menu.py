#!/usr/bin/env python3

#车型库,非关系型数据库
cars_dic = {'一汽大众':{'宝来':
                            ['宝来1.6','宝来1.4T'],
                       '迈腾':
                            ['迈腾1.8T','迈腾2.0T']
                       },
            '上海大众':{'朗逸':
                             ['朗逸1.6','朗逸1.4T'],
                       '帕萨特':
                             ['帕瑟特1.8T','帕萨特2.0T']
                      }
            }




d = 0                          #配合最后判断是否继续循环使用的初始值
while d == "继续" or d == 0:    #多次查询的循环,客户自己确认是否继续
    print("欢迎您登入汽车之家,以下是所有的汽车品牌")
    car_pinpai = list(cars_dic.keys())              #将字典中第一层的key,抓取出来并做成列表
    for pinpai in car_pinpai:                       #遍历显示字典中第一层所有的key
        print("汽车品牌:%s" %(pinpai))


    inp_pinpai = input("请输入你想了解的汽车品牌:")        #输入想要的key
    if inp_pinpai in car_pinpai:                       #如果输入的key在字典第一层key中,执行下方操作
        car_chexing = cars_dic.get(inp_pinpai).keys()        #取出字典中,指定的第一层key,所包含的所有第二层key,并作为字典,赋值给变量,
        print("一汽大众车型有")
        for b in car_chexing:                          #遍历显示字典中指定的第一层key,所包含的第二层key
            print(b)
    else:                                               #如果输入的key不再字典第一层key中,执行下方操作
            print("输入有误,将返回上层界面")
            continue                                    #退出本次循环

    inp_chexing = input("请输入你想了解的车型:")
    if inp_chexing in car_chexing:
        print("%s车型包含以下型号:" %(inp_chexing))
        for c in cars_dic.get(inp_pinpai).get(inp_chexing):
            print(c)
    else:
        print("输入有误,将返回上层界面")
        exit()
    d = input("是否继续查询: 继续  or  退出")
