'''

configparser 模块可以生成配置文件

[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no

'''


import configparser

config = configparser.ConfigParser()   #声明一个对象

config["DEFAUTL"] = {'ServerAliveInterval':'45',
                     'Compression':'yes',
                     'CompressionLevel':'9'}


config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'

with open('config.ini','w') as configfile:
    config.write(configfile)