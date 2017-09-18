'''
读取config.ini


configparser 模块可以生成配置文件

[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg
ForwardX11 = yes

[topsecret.server.com]
Port = 50022
ForwardX11 = no


'''

import configparser

config = configparser.ConfigParser()

config.read('config.ini')


########读---查###########

# secs = config.sections()                 #['DEFAUTL', 'bitbucket.org', 'topsecret.server.com']
#
# config.read('config.ini')
#
# print(secs)
#
# print(config.options('bitbucket.org'))       #['user', 'forwardx11']
# print(config.items('bitbucket.org'))         #[('forwardx11', 'yes'), ('user', 'hg')]
# print(config.get('bitbucket.org','user'))    #hg
#
#
# for i in config:
#     print(i)


############改--增删改#########

#
# print(config.items('bitbucket.org'))
# print(config.remove_section('bitbucket.org'))         #删除 bitbucket.org section
# print(config.remove_option('bitbucket.org','user'))      #删除一个option
# print(config.sections())
# config.write(open('config-remove.ini','w'))          #将删除后的内容,写入到文件


sec = config.has_section('timo')
sec = config.add_section('timo')          #增加一个section
config['timo']['age'] = '11'              #向timo的section中增加内容
config.write(open('config_add.ini','w'))


config.set('timo','age','22')          #修改内容
config.write(open('config_put.ini','w'))
