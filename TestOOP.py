#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self,name):
		self._name=name

	def __str__(self):
		return "这里返回实例字符串"+self._name

	#__repr__ = __str__

s1=Student('cs')
s1
print(s1)



class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
	print(n)


#枚举

from enum import Enum,unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 7

print(Weekday.Mon)
print(Weekday(7))

@unique
class Gender(Enum):
    Male=0
    Female=1

class Employee(object):
	def __init__(self,name,gender):
		self._name=name
		self._gender=gender
testEmployee=Employee('cs',Gender.Female)

print(testEmployee._gender==Gender.Male)


#引入模块，一个py文件可以放置多个类
from module.hello import Hello,Test
h=Hello("python3")
#from module.hello import Test
test=Test("test")
t=test.test()

print(type(Hello))
print(type(h))

#metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为


#异常处理

try:
	result=10/0
	print(result)
except ZeroDivisionError  as e:
	#raise ZeroDivisionError('invalid value:')
	print('except:',e)
else:
	print('no error')
finally:
	print("end")

import logging
logging.basicConfig(level=logging.INFO)

logging.info("test....")
		
		
