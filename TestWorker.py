

import time
import sys
import queue
from multiprocessing.managers import BaseManager


class MyQueueManager(BaseManager):
    pass


def start():
    MyQueueManager.register('get_task_queue')
    MyQueueManager.register('get_result_queue')

    server_addr = '127.0.0.1'
    print('conect to sever %s' % server_addr)
    m = MyQueueManager(address=(server_addr, 5000), authkey=b'abc')
    m.connect()

    task = m.get_task_queue()
    result = m.get_result_queue()

    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d....' % (n, n))
            r = n * n
            time.sleep(1)
            result.put(r)
        except queue.empty:
            print('task queue is empty')

    print('worker exit...')


if __name__ == '__main__':
    start()
