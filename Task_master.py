

# 主任务

import random
import time
import queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()

result_queue = queue.Queue()


class MyQueueManager(BaseManager):
    pass


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def start():
    MyQueueManager.register("get_task_queue", callable=return_task_queue)
    MyQueueManager.register('get_result_queue', callable=return_result_queue)

    manager = MyQueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print("put a task %d ..." % n)
        task.put(n)

    print('try get results...')
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('result: %s ...' % r)
        except queue.Empty:
            print('main task queue is empty...')

    manager.shutdown()
    print("master exit")


# window 运行
if __name__ == '__main__':
    start()
