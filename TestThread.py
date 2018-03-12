

# #线程访问
# import time ,threading

# def loop():
# 	print('thread %s is running...' %threading.current_thread().name)

# 	n=0
# 	while n<5:
# 		n=n+1
# 		print('thread %s >>> %s' %(threading.current_thread().name,n))
# 		time.sleep(1)
# 	print("thread %s ended..." %threading.current_thread().name)


# print('thread %s is running....' %threading.current_thread().name)
# t=threading.Thread(target=loop,name='testLoopThread')
# t.start()
# #等待线程执行结束
# # t.join()
# print('thread % s is ended...' %threading.current_thread().name)


# 线程锁
# import time,threading

# balance=0
# lock = threading.Lock()

# def change(n):
# 	#使用全局变量
# 	global balance
# 	balance=balance+n
# 	balance=balance-n

# #不加锁的情况会导致计算出错
# def run_thread(n):
# 	for i in range(100000):
# 		change(n)

# def run_thread_with_lock(n):
# 	for i in range(100000):
# 		lock.acquire()
# 		try:
# 			change(n)
# 		finally:
# 			lock.release()

# # t1=threading.Thread(target=run_thread,args=(5,))
# # t2=threading.Thread(target=run_thread,args=(99,))
# t1=threading.Thread(target=run_thread_with_lock,args=(5,))
# t2=threading.Thread(target=run_thread_with_lock,args=(99,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 获取当前机器cpu个数
# import multiprocessing
# print(multiprocessing.cpu_count())

# ThreadLocal 实现线程内独立的全局变量，每个线程一个单独的副本
import threading

# 全局ThreadLocal对象
local_data = threading.local()


def process_data():
    # 获得当前线程的参数
    data = local_data.name
    print('get the local data:', data)


def process_thread(name):
    # 绑定当前线程的参数
    local_data.name = name
    process_data()


t1 = threading.Thread(target=process_thread, args=('test1',))
t2 = threading.Thread(target=process_thread, args=('test2',))
t1.start()
t2.start()
t1.join()
t2.join()
