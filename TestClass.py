#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

print("test")

#print(dir("abc"))

print(isinstance("str",str))

print(len("abc"))
print("abc".__len__())


#获取对象属性和方法
class MyObject(object):
    def __init__(self):
        self.x=33

    def power(self):
        return self.x*self.x

obj=MyObject()

print(hasattr(obj,'x'))
print(getattr(obj,'y',22))
fn=getattr(obj,'power')
print(fn())


#类属性与实例属性
class Student(object):
    #用以限制实例的属性，对子类不起作用
    __slots__=("age","name","_score")

    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1
        #print(Student.count)

    #getter
    @property
    def score(self):
        return self._score

    #setter
    @score.setter
    def score(self,value):
        self._score=value


s1=Student("s1")
print(Student.count)
s2=Student("s2")
print(Student.count)
s3=Student("s3")
print(Student.count)

#给类绑定方法
def set_age(self,age):
    self.age=age

Student.set_age=set_age

ss=Student("cs")
ss.set_age(123)
print(ss.age)

ss.score=999
print(ss.score)

