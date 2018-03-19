

# namedtuple	自定义tuple对象

from collections import namedtuple
TestPoint = namedtuple('Point', ['x', 'y'])

p = TestPoint(3, 4)

print(p.x, p.y)


# deque 双向队列 list（线性存储，查找快，插入删除慢）

from collections import deque

q = deque(['x', 'y', 'z'])
# 可以对最左元素进行操作
q.popleft()
q.appendleft('a')
print(q)


# defaultdict	有默认值的字典
from collections import defaultdict


def dict_default_vaule():
    return "test1"


# dd=defaultdict(lambda:'null')
dd = defaultdict(dict_default_vaule)
dd['key1'] = 'test'
print(dd['key1'])
print(dd['key2'])


# OrderedDict	有序集合，顺序是按照插入的顺序来的
from collections import OrderedDict
d = dict([('b', 1), ('a', 2), ('c', 4)])
print(d)

od = OrderedDict([('b', 1), ('a', 2), ('c', 4)])
print(d)


# Counter	计数器 统计字符出现个数等
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

#是一个字典的子类
print(isinstance(c, dict))
print(c)
print(Counter('testing'))