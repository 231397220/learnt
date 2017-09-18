


'''
os模块
python 需要和 操作系统 交互时,可以使用os模块

>>> os.chdir("/Users/Sam/")  类似于  cd /users/sam/
>>> os.getcwd()     获取当前目录
'/Users/Sam'
>>> os.chdir("/Users/Sam/PycharmProjects/learnt_git/python")   返回当前目录

>>> os.getcwd()
'/Users/Sam/PycharmProjects/learnt_git/python'

os.pardir  返回当前目录的父目录字符串名

os.makedirs('dirname1/dirname2') 生产多层递归目录

os.removedirs('dirname1')     递归删除空目录,若目录为空,则删除,并递归到上一级目录,如果上一级目录也是空,则删除

os.mkdir("dirname")   创建单级目录

os.rmdir('dirname')   删除单级目录

>>> os.listdir("/Users/Sam/PycharmProjects/learnt_git/")
['.git', 'python']

>>> os.stat('/Users/Sam/PycharmProjects/learnt_git/')
os.stat_result(st_mode=16877, st_ino=18221465, st_dev=16777220, st_nlink=4, st_uid=501, st_gid=20, st_size=136, st_atime=1505372111, st_mtime=1504250858, st_ctime=1504250858)

>>> os.name         输出字符串指示当前使用平台 win=nt  linux=posix
'posix'

>>> os.system("pwd")   运行shell命令
/Users/Sam/PycharmProjects/learnt_git/python


>>> os.environ   获取操作系统环境变量
environ({'TERM_PROGRAM': 'iTerm.app', 'TERM': 'xterm-256color', 'SHELL': '/bin/bash', 'TMPDIR': '/var/folders/1t/mtbtj2r91l9d_xt1s38n40rh0000gn/T/', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.APMIgk3o8L/Render', 'TERM_PROGRAM_VERSION': '3.0.15', 'TERM_SESSION_ID': 'w0t4p0:D4A2EDA6-F346-46E0-83DE-1548C96ED903', 'USER': 'Sam', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.laun

os.rename("oldname","newname") 改文件名

os.path.abspath(path)返回path规范化的绝对路径
os.path.split(path) 将path分割成目录和文件名二元组返回
os.path.dirname(path) 返回path的目录.
os.path.basename(path) 返回path最后的文件名
os.path.exists(path) 如果path存在,返回True, 如果path不存在,返回Frous
os.path.isabs(path) 如果path是绝对路径,返回True
os.path.isdir() 是不是dir
os.path.join(path1[,path2[,...]])





sys

sys.argv 命令行参数list,第一个元素是程序本身路径
sys.exit(n)   退出程序  n=pring(bey)
sys.path  返回模块的所搜路径
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']

>>> sys.platform    返回操作系统平台名称
'darwin'





'''