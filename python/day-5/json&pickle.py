

'''
pickle 和 json  都只有4个功能

pickle.dump = pickle.dump(info,f)

pickle.load  = pickle.loads(f.read())


'''

#序列化  字符串 转变 字典

import pickle
import json


name = ['sam','timo','jason']

f = open('pickle_test','wb')
pickle.dump(name,f)

pickle.dump('test',f)

f.close()