

# 操作迭代器对象


# count
# 死循环
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)


import itertools
ns = itertools.repeat('abc', 2)
for n in ns:
    print(n)


# chain 串联迭代器
for c in itertools.chain('abc', 'def'):
    print(c)


# groupby 把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('aaabbBcCaacc'):
    print(key, list(group))


for key, group in itertools.groupby('aaabbBcCaacc', lambda x: x.upper()):
    print(key, list(group))
