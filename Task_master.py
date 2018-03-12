

# 主任务

import random
import time
import queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()

result_queue = queue.Queue()


class MyQueueManager(BaseManager):
    pass


MyQueueManager.register("get_task_queue", callable=lambda: task_queue)
MyQueueManager.register('get_result_queue', callable=lambda: result_queue)

manager = MyQueueManager(address=('', 3333), authkey=b'abc')

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random(0, 10000)
    print("put a task %d ..." % n)
    task.put(n)


print('try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('result: %s ...' % r)


manager.shutdown()
print("master exit")
