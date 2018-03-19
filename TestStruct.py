

import struct
# 转换成二进制
b = struct.pack('>I', 123)
bb = struct.pack('>H', 123)
print(b)
print(bb)


# 读取图片的二进制编码并解析

# I表示4字节无符号整数
# H：2字节无符号整数
# c:单字节 字符

#>表示字节顺序是big-endian
#< small-endian
import struct

file_object = open('test.bmp', 'rb')
info = file_object.read()[:2]
#bt = struct.unpack('<ccIIIIIIHH', info)
bt = struct.unpack('<cc', info)
file_object.close()
print(info)
print(bt)
print(bt[0] in [b'B'])
print(bt[1])
