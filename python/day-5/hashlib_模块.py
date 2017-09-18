'''
hash 散列算法
hashlib 加密模块   在 3.x  中 取代了 MD5 ,SHA


'''


import hashlib

m = hashlib.md5()
m.update(b"Hello")
m.update(b"It's me")
print(m.digest())
m.update(b"It's been a long time since last time we ...")

print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash


'''
>>> a.update(b"hello")
>>> a.digest()
b']A@*\xbcK*v\xb9q\x9d\x91\x10\x17\xc5\x92'
>>> a.hexdigest()
'5d41402abc4b2a76b9719d911017c592'



'''


#
# import hmac
# h = hmac.new(b'天王盖地虎', b'宝塔镇河妖')
# print (h.hexdigest())