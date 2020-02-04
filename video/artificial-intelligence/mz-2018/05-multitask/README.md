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







