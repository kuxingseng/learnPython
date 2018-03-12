

f=open("test.txt","w")
f.write("hello io test")
f.close()
f=open("test.txt","r")
print(f.read())


with open("test.txt","a") as f:
	f.write(" world")

#自动执行close操作
with open("test.txt","r") as f:
	print(f.read())


from io import StringIO
f=StringIO("Helllo,\n Hi!\nGoodbye!")
print(f.getvalue())
while True:
	s=f.readline()
	if s=="":
		break

	print(s.strip())



import os
#print(os.environ)

print("当前目录："+os.path.abspath('.'))
os.path.join(os.path.abspath('.'),'testdir')
#os.mkdir(os.path.join(os.path.abspath('.'),'testdir'))
#os.rmdir(os.path.join(os.path.abspath('.'),'testdir'))

#筛选当前目录下所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


#序列化、反序列化
import pickle
d= dict(name='chenshuai',age=30)
print(pickle.dumps(d))

#写入文件
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

#从文件读取并反序列化
f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)


# 使用json
print('-----------')
import json
d= dict(name='chenshuai',age=30)
js=json.dumps(d)
print(js)

#序列化类
class Student(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	#指定序列化的方式
	def student2dict(std):
		return{
			'name':std.name
		}
		return{
			'name':std.name,
			'age':std.age
		}

	#指定反序列化方式
	def dict2student(d):
		return Student(d['name'],d['age'])

s=Student("cs",22)


print(json.dumps(s,default=Student.student2dict))

#默认的序列化方式
print(json.dumps(s,default=lambda obj:obj.__dict__))

#反序列化
json_str=json.dumps(s,default=lambda obj:obj.__dict__)
print(json.loads(json_str,object_hook=Student.dict2student))