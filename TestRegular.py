

import re

result = re.match(r'^\d{3}-\d{3,8}$', '010-12345')
print(result)

# result = re.match(r'^\d{3}-\d{3,8}$', '010 12345')
# print(result)

if(result):
    print('ok')
else:
    print('fail')


# 识别连续的空格
print(re.split(r'\s+', 'a b    c'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
