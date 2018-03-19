

# Base64是一种用64个字符来表示任意二进制数据的方法。
# 每6个bit转换为一个字符

import base64

b64_encode = base64.b64encode(b'test')
print(b64_encode)
b64_decode = base64.b64decode(b64_encode)
print(b64_decode)


def safe_base64_decode(s):
	# 数字乘以字符，等于数字个字符组成的字符串
    s = s + len(s) % 4 * b'='
    return base64.b64decode(s)


print(safe_base64_decode(b'dGVzdA'))
print(5 * 't')
