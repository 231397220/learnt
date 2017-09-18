import re

'''
^ 匹配开头
[^]  中括号中使用为 非
$ 匹配末尾
. 匹配任意字符
.+ 匹配任意字符一个或多个
[...]  匹配中括号中的内容
[()]   匹配 '(' 和 ')'
* 匹配 0 个或多个
+ 匹配一个或多个
? 匹配0 个或一个
{n} 匹配N次
\d 匹配一个数字
|   或的意思
() 匹配括号内的表达式
\w 匹配字母或者数字
\W 匹配非字母或数字
\s 匹配认识空白字符
\S 匹配非空白字符
\b 匹配一个单词的边界


match 从头匹配
search  匹配整个字符串
split   将匹配到的格式当做分割点对字符串分割成列表
findall  找到所有要匹配的字符
sub     替换所有要匹配的字符            count=2   只替换2次




'''


string = '192.168.2.2'
m = re.match("([0-9]{1,3}\.){3}\d{1,3}",string)
print(m.group())

m = re.split("[0-9]", "sam1timo2jason3helen read8")
print(m)

m = re.findall("[0-9]","sam1timo2jason3helen read8")
print(m)

m = re.sub("[0-9]","|","sam1timo2jason3helen read8",count=2)
print(m)