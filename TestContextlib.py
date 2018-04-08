

# 上下文管理 自动实现类开始和结束时要执行的逻辑

# 如 open()

with open('test.txt', 'r') as f:
    print(f.read())


# 任何对象，只要正确实现了上下文管理，就可以用于with语句。

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('begin....')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("error", exc_type)
        else:
            print('end')

    def query(self):
        print('query info about %s ' % self.name)


with Query('chenshuai') as q:
    q.query()


# contextmanager Python的标准库contextlib提供了更简单的写法

from contextlib import contextmanager


class MyQuery(object):
    """docstring for MyQuery"""

    def __init__(self, name):
        self.name = name

    def query(self):
        print('query info about %s ' % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = MyQuery(name)
    yield q
    print('end')


with create_query('chen shuai') as q:
    q.query()
