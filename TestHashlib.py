

# #什么是摘要算法呢？
# 摘要算法又称哈希算法、散列算法。
# 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
# （通常用16进制的字符串表示）


# md5

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python'.encode('utf-8'))
print(md5.hexdigest())

# sha1
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python'.encode('utf-8'))
print(sha1.hexdigest())


# hmac

import hmac

message = b'hello world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())
