


'''
U 处理换行符,把windows和linux的换行符都转换成\n

close  关闭
fileno   文件描述符
flush  从内存刷进硬盘
read   读取所有内容,可执行读指定字符,FTP上传1024kb.
readline   只读取一行
seek       指定当前指针位置
tell       查看当前指针位置
truncate(n)    保留指针前内容



'''

f = open('test.log','r',encoding='utf-8')
# f.write('dafdagdagdsagda')
# ret = f.read(2)
# print(f.tell())


f.seek(5)
print(f.read())
# print(f.truncate())
f.close()

print(ret)
