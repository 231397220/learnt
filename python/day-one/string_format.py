#!/usr/bin/env python3
#万恶的+号,能不用就不用
name = input("name:").strip("zha")
age = int(input("age:"))
job = input("job:").strip()

#print("Infomation of []:"+ name +"\n Name:[]"+ name +"\n Age:[]"+ age +"\n Job:[]+ job")
print("infomation of %s:\nName:%s\nAge:%s\nJob:%s"  %(name,name,age,job))



# %d  代表数字
# %f  代表小数
# %s  代表变量
msg = '''
information of: %s
Name: %s
Age: %d
Job: %s
''' %(name,name,age,job)
print(msg)