# 五 多任务
* 并发：指的是任务数多余cpu核数，通过操作系统的各种任务调度算法，实现用多个任务“一起”执行（实际上总有一些任务不在执行，因为切换任务的速度相当快，看上去一起执行而已）
* 并行：指的是任务数小于等于cpu核数，即任务真的是一起执行的

## 5.1 线程
### 5.1.1 使用threading模块
* 单线程执行
```python
#coding=utf-8
import time

def saySomething():
    print("say something")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        saySomething()
```

* 多线程执行
```python
#coding=utf-8
import threading
import time

def saySomething():
    print("say something")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySomething)
        t.start() #启动线程，即让线程开始执行
```


### 5.1.2 线程执行代码的封装
```python
#coding=utf-8
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i) #name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    t.start()
```

## 5.2 进程

### 5.2.1 进程的创建-multiprocessing
> multiprocessing模块就是跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象，这个对象可以理解为是一个独立的进程，可以执行另外的事情

>创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动


### 5.2.2 进程pid
```python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
import time

def run_proc():
    """子进程要执行的代码"""
    print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
    print('子进程将要结束...')

if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()
```

### 5.2.3 Process语法结构
* Process([group [, target [, name [, args [, kwargs]]]]])
    * target：如果传递了函数的引用，可以任务这个子进程就执行这里的代码
    * args：给target指定的函数传递的参数，以元组的方式传递
    * kwargs：给target指定的函数传递命名参数
    * name：给进程设定一个名字，可以不设定
    * group：指定进程组，大多数情况下用不到
* Process创建的实例对象的常用方法：
    * start()：启动子进程实例（创建子进程）
    * is_alive()：判断进程子进程是否还在活着
    * join([timeout])：是否等待子进程执行结束，或等待多少秒
    * terminate()：不管任务是否完成，立即终止子进程
* Process创建的实例对象的常用属性：
    * name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
    * pid：当前进程的pid（进程号）

### 5.2.4 进程间通信-Queue
> Process之间有时需要通信，操作系统提供了很多机制来实现进程间的通信。

#### 5.2.4.1 Queue的使用
```python
#coding=utf-8
from multiprocessing import Queue
q=Queue(3) #初始化一个Queue对象，最多可接收三条put消息
q.put("消息1") 
q.put("消息2")
print(q.full())  #False
q.put("消息3")
print(q.full()) #True

#因为消息列队已满下面的try都会抛出异常，第一个try会等待2秒后再抛出异常，第二个Try会立刻抛出异常
try:
    q.put("消息4",True,2)
except:
    print("消息列队已满，现有消息数量:%s"%q.qsize())

try:
    q.put_nowait("消息4")
except:
    print("消息列队已满，现有消息数量:%s"%q.qsize())

#推荐的方式，先判断消息列队是否已满，再写入
if not q.full():
    q.put_nowait("消息4")

#读取消息时，先判断消息列队是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
```

* 初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；
    * Queue.qsize()：返回当前队列包含的消息数量；
    * Queue.empty()：如果队列为空，返回True，反之False ；
    * Queue.full()：如果队列满了，返回True,反之False；
    * Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；
        * 如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；
        * 如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；
    * Queue.get_nowait()：相当Queue.get(False)；
    * Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True；
        * 如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间为止，如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；
        * 如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；
    * Queue.put_nowait(item)：相当Queue.put(item, False)；


### 5.2.5 进程池Pool
> 如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()
```python


# -*- coding:utf-8 -*-

# 修改import中的Queue为Manager
from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))

def writer(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "itcast":
        q.put(i)

if __name__=="__main__":
    print("(%s) start" % os.getpid())
    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool()
    po.apply_async(writer, (q,))

    time.sleep(1)  # 先让上面的任务向Queue存入数据，然后再让下面的任务开始从中取数据

    po.apply_async(reader, (q,))
    po.close()
    po.join()
    print("(%s) End" % os.getpid())

```


## 5.3 协程
> 协程是python个中另外一种实现多任务的方式，只不过比线程更小占用更小执行单元

### 5.3.1 迭代器
> 可以通过for...in...这类语句迭代读取一条数据供我们使用的对象称之为可迭代对象（Iterable）

* 如何判断一个对象是否可以迭代
```python
# 可以使用 isinstance() 判断一个对象是否是 Iterable 对象：
from collections import Iterable
print(isinstance([], Iterable))
```

### 5.3.2 生成器
### 5.3.3 协程-yield
* 协程和线程差异
    *在实现多任务时, 线程切换从系统层面远不止保存和恢复 CPU上下文这么简单。 操作系统为了程序运行的高效性每个线程都有自己缓存Cache等等数据，操作系统还会帮你做这些数据的恢复操作。 所以线程的切换非常耗性能。但是协程的切换只是单纯的操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住。

* 简单实现协程
```python

import time

def work1():
    while True:
        print("----work1---")
        yield
        time.sleep(0.5)

def work2():
    while True:
        print("----work2---")
        yield
        time.sleep(0.5)

def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)

if __name__ == "__main__":
    main()

```

### 5.3.4 协程-greenlet
> 为了更好使用协程来完成多任务，python中的greenlet模块对其封装，从而使得切换任务变的更加简单

* 安装方式
    * 使用如下命令安装greenlet模块:
    > sudo pip3 install greenlet
```python
                                
#coding=utf-8
from greenlet import greenlet
import time

def test1():
    while True:
        print "---A--"
        gr2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print "---B--"
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

#切换到gr1中运行
gr1.switch()

```   


### 5.3.5 协程-gevent
> python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent  
>>其原理是当一个greenlet遇到IO(指的是input output 输入输出，比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO

* 安装
> pip3 install gevent

* gevent的使用
```python

import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

```

### 5.3.6 进程、线程、协程对比
* 进程是资源分配的单位
* 线程是操作系统调度的单位
* 进程切换需要的资源很最大，效率很低
* 线程切换需要的资源一般，效率一般（当然了在不考虑GIL的情况下）
* 协程切换任务资源很小，效率高
* 多进程、多线程根据cpu核数不一样可能是并行的，但是协程是在一个线程中 所以是并发








