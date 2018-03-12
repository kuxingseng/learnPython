

# from multiprocessing import Process
# import os,time,random

# #定义子进程方法

# def run_child_proc(name):
# 	#睡眠一段时间
# 	time.sleep(random.random()*3)
# 	print('Run child process %s(%s)...' %(name,os.getpid()))


# if __name__ == '__main__':
# 	print('parent process %s.' %os.getpid())
# 	p=Process(target=run_child_proc,args=('test',))
# 	print('child process will start...')
# 	#启动进程
# 	p.start()
# 	#等待进程执行完成
# 	p.join()
# 	print('child process end...')


# print('--------------------------------')
# #使用进程池
# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
# 	print('run task %s (%s)...' %(name, os.getpid()))
# 	start=time.time()
# 	time.sleep(random.random())
# 	end = time.time()
# 	print('task %s runs %0.2f secends...' %(name, (end-start)))

# if __name__ == '__main__':
# 	print('parent process %s..' %os.getpid())
# 	p=Pool(8)
# 	for i in range(9):
# 		p.apply_async(long_time_task,args=(i,))

# 	print('waiting for all subprocess done...')
# 	p.close()
# 	p.join()
# 	print('all subprocess done....')



# #子进程
# import subprocess
# print('$ nslookup www.baidu.com')
# r=subprocess.call(['nslookup','www.python.org'])
# print('exit code :',r)


#进程之间通信
from multiprocessing import Process,Queue
import os,time,random

def write(q):
	print('process to write:%s ' %os.getpid())
	for value in ['a','b','c']:
		print('put %s into queue' %value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('process to read %s ' %os.getpid())
	while True:
		value=q.get(True)
		print('get %s from queue...' %value)

if __name__ == '__main__':
	#在父进程中创建查询
	q=Queue()
	pw=Process(target=write,args=(q,))
	pr=Process(target=read,args=(q,))

	pw.start()
	pr.start()

	pw.join()

	pr.terminate()