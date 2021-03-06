# 二 面向对象

## 2.1 面相对象基础语法

### 2.1.1 dir 内置函数

\__方法名__ 格式的方法是 Python 提供的 内置方法 / 属性


|序号|方法名|类型|作用|
|---|-----|----|---|
|01|\_\_new__|方法|创建对象时，会被 自动 调用|
|02|\_\_init__|方法|对象被初始化时，会被 自动 调用|
|03|\_\_del__|方法|对象被从内存中销毁前，会被 自动 调用|
|04|\_\_str__|方法|返回对象的描述信息，print 函数输出使用|

### 2.1.2 定义简单的类
* 在 Python 中要定义一个只包含方法的类，语法格式如下：
```python
class 类名:

    def 方法1(self, 参数列表):
        pass
    
    def 方法2(self, 参数列表):
        pass

```
* 方法 的定义格式和上面学习过的函数 几乎一样，区别在于第一个参数必须是 self

### 2.1.3 创建对象
当一个类定义完成之后，要使用这个类来创建对象，语法格式如下：
```
对象变量 = 类名()
```


### 2.1.4 类的引用
* 在 Python 中使用类 创建对象之后，变量中记录的是 对象在内存中的地址，引用了新建的锚对象
* 使用 print 输出 对象变量，默认情况下，是能够输出这个变量引用的对象是由哪一个类创建的对象，以及在内存中的地址（十六进制表示）
> 在计算机中，通常使用 十六进制 表示 内存地址  
* %d 可以以 10 进制 输出数字
* %x 可以以 16 进制 输出数字

### 2.1.5 方法中的 self 参数
#### 2.1.5.1 给对象增加属性
* 在 Python 中，要 给对象设置属性，只需要在类的外部的代码 中直接通过`.`设置一个属性即可
```
object.name = "name"
```
> 不推荐使用，因为对象属性的封装应该封装在类的内部
#### 2.1.5.2 使用 self 在方法内部输出对象的属性
* 由 哪一个对象 调用的方法，方法内的 self 就是 哪一个对象的引用
* 在类封装的方法内部，self 就表示 当前调用方法的对象自己
* 调用方法时，程序员不需要传递 self 参数
* 在方法内部
    * 可以通过 self. 访问对象的属性
    * 也可以通过 self. 调用其他的对象方法
* 在类的外部，通过变量名. 访问对象的属性和方法
* 在类封装的方法中，通过 self. 访问对象的属性和方法

### 2.1.6 初始化方法
* 当使用类名() 创建对象时，会自动执行以下操作：
    * 为对象在内存中 分配空间 —— 创建对象
    * 为对象的属性 设置初始值 —— 初始化方法(init)
* 这个初始化方法就是 \_\_init__ 方法，\_\_init__ 是对象的内置方法
* \_\_init__ 方法是专门用来定义一个类具有哪些属性

#### 2.1.6.1 在初始化方法内部定义属性
* 在 \_\_init__ 方法内部使用 self.属性名 = 属性的初始值 就可以 定义属性
* 定义属性之后，再使用类创建的对象，都会拥有该属性

### 2.1.7 内置方法和属性

|序号|方法名|类型|作用|
|---|-----|----|---|
|01|\_\_del__|方法|对象被从内存中销毁前，会被自动调用|
|02|\_\_str__|方法|返回对象的描述信息，print 函数输出使用|

#### 2.1.7.1 \_\_del__ 方法
* 在 Python 中
    * 当使用 类名() 创建对象时，为对象分配完空间后，自动调用 \_\_init__ 方法
    * 当一个对象被从内存中销毁 前，会自动调用\_\_del__方法
* 应用场景
    * \_\_init__改造初始化方法，可以让创建对象更加灵活
    * \_\_del__如果希望在对象被销毁前，再做一些事情，可以考虑一下\_\_del__方法
* 生命周期
    * 一个对象从调用类名()创建，生命周期开始
    * 一个对象的\_\_del__方法一旦被调用，生命周期结束
    * 在对象的生命周期内，可以访问对象属性，或者让对象调用方法

#### 2.1.7.2 \_\_str__ 方法
* 在 Python 中，使用 print输出对象变量，默认情况下，会输出这个变量 引用的对象是由哪一个类创建的对象，以及在内存中的地址（十六进制表示）
* 如果在开发中，希望使用print输出对象变量时，能够打印自定义的内容，就可以利用 \_\_str__ 这个内置方法了


### 2.1.8 身份运算符
* 身份运算符用于比较两个对象的内存地址是否一致 —— 是否是对同一个对象的引用
* 在 Python中针对None比较时，建议使用 is 判断

|运算符|描述|实例|
|-----|---|----|
|is|is|是判断两个标识符是不是引用同一个对象	x is y，类似 id(x) == id(y)|
|is not|is not|是判断两个标识符是不是引用不同对象	x is not y，类似 id(a) != id(b)|

* is 与 == 区别：
    * is 用于判断 两个变量 引用对象是否为同一个 
    * == 用于判断 引用变量的值 是否相等

### 2.1.9 私有属性和私有方法
* 定义方式
    * 在定义属性或方法时，在属性名或者方法名前增加两个下划线，定义的就是私有属性或方法

### 2.1.10 伪私有属性和私有方法
> Python 中，并没有真正意义的私有

* 在给属性、方法命名时，实际是对名称做了一些特殊处理，使得外界无法访问到
* 处理方式：在名称前面加上_类名 =>_类名__名称

## 2.2 继承

面向对象三大特性

* 封装:根据 职责 将 属性 和 方法 封装 到一个抽象的 类 中
* 继承:实现代码的重用，相同的代码不需要重复的编写
* 多态:不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度


### 2.2.1 单继承
* 继承的概念：
    * 子类拥有父类的所有方法和属性

* 继承的语法:
```
class 类名(父类名):
    pass
```


### 2.2.2 方法的重写
* 当父类的方法实现不能满足子类需求时，可以对方法进行重写(override)
* 重写父类方法有两种情况：
    * 覆盖父类的方法：实现完全不同
    * 对父类方法进行扩展：super().父类方法
    
    
### 2.2.3 父类的 私有属性 和 私有方法
* 子类对象不能在自己的方法内部，直接访问父类的私有属性或私有方法
* 子类对象可以通过父类的公有方法间接访问到私有属性或私有方法

### 2.2.4 多继承
语法
```
class 子类名(父类名1, 父类名2...)
    pass
```

### 2.2.5 多继承的使用注意事项
* 如果 父类之间 存在 同名的属性或者方法，应该 尽量避免 使用多继承

#### 2.2.5.1 Python 中的 MRO —— 方法搜索顺序
* Python 中针对 类 提供了一个 内置属性 \_\_mro__ 可以查看 方法 搜索顺序
* MRO 是 method resolution order，主要用于 在多继承时判断 方法、属性 的调用 路径
```
print(C.\_\_mro\_\_)
```
输出结果
```
(<class '\_\_main\_\_.C'>, <class '\_\_main\_\_.A'>, <class '\_\_main\_\_.B'>, <class 'object'>)
```
* 在搜索方法时，是按照 \_\_mro\_\_ 的输出结果 从左至右 的顺序查找的
* 如果在当前类中 找到方法，就直接执行，不再搜索
* 如果 没有找到，就查找下一个类 中是否有对应的方法，如果找到，就直接执行，不再搜索
* 如果找到最后一个类，还没有找到方法，程序报错

### 2.2.6 新式类与旧式（经典）类
* object 是 Python 为所有对象提供的 基类，提供有一些内置的属性和方法，可以使用 dir 函数查看
* 新式类：以 object 为基类的类，推荐使用
* 经典类：不以 object 为基类的类，不推荐使用
* 在 Python 3.x 中定义类时，如果没有指定父类，会 默认使用 object 作为该类的 基类 —— Python 3.x 中定义的类都是 新式类
* 在 Python 2.x 中定义类时，如果没有指定父类，则不会以 object 作为 基类
* 新式类 和 经典类 在多继承时 —— 会影响到方法的搜索顺序
    * 为了保证编写的代码能够同时在 Python 2.x 和 Python 3.x 运行！
    * 今后在定义类时，如果没有父类，建议统一继承自 object
```
class 类名(object):
    pass
```

## 2.3 多态
* 多态 不同的 子类对象 调用相同的 父类方法，产生不同的执行结果
    * 多态 可以 增加代码的灵活度
    * 以 继承 和 重写父类方法 为前提
    * 是调用方法的技巧，不会影响到类的内部设计

## 2.4 类属性和类方法
### 2.4.1 类属性和类方法
* 通常也会把：
    * 创建出来的对象叫做类的实例
    * 创建对象的动作叫做实例化
    * 对象的属性叫做实例属性
    * 对象调用的方法叫做实例方法
* 在程序执行时：
    * 对象各自拥有自己的实例属性
    * 调用对象方法，可以通过self.
        * 访问自己的属性
        * 调用自己的方法
* 结论
    * 每一个对象都有自己独立的内存空间，保存各自不同的属性
    * 多个对象的方法，在内存中只有一份，在调用方法时，需要把对象的引用 传递到方法内部
* 类是一个特殊的对象
    * Python 中 一切皆对象：
        * class AAA: 定义的类属于 类对象
        * obj1 = AAA() 属于 实例对象
    * 在程序运行时，类 同样 会被加载到内存
    * 在 Python 中，类 是一个特殊的对象 —— 类对象
    * 在程序运行时，类对象 在内存中 只有一份，使用 一个类 可以创建出 很多个对象实例
    * 除了封装 实例 的 属性 和 方法外，类对象 还可以拥有自己的 属性 和 方法
        * 类属性
        * 类方法
    * 通过 类名. 的方式可以 访问类的属性 或者 调用类的方法

### 2.4.2 类属性和实例属性
#### 2.4.2.1 概念和使用
* 类属性 就是给 类对象 中定义的 属性
* 通常用来记录 与这个类相关 的特征
* 类属性 不会用于记录 具体对象的特征

#### 2.4.2.2 属性的获取机制
* 在 Python 中 属性的获取 存在一个 向上查找机制
    * 要访问类属性有两种方式：
        * 类名.类属性
        * 对象.类属性 （不推荐）
    * 如果使用 对象.类属性 = 值 赋值语句，只会 给对象添加一个属性，而不会影响到 类属性的值

#### 2.4.2.3 类方法和静态方法
* 类方法
    * 类属性 就是针对 类对象 定义的属性
        * 使用 赋值语句 在 class 关键字下方可以定义 类属性
        * 类属性 用于记录 与这个类相关 的特征
    * 类方法 就是针对 类对象 定义的方法
        * 在 类方法 内部可以直接访问 类属性 或者调用其他的 类方法
    * 类方法需要用 修饰器 @classmethod 来标识，告诉解释器这是一个类方法
    * 类方法的 第一个参数 应该是 cls
        * 由 哪一个类 调用的方法，方法内的 cls 就是 哪一个类的引用
        * 这个参数和 实例方法 的第一个参数是 self 类似
        * 提示 使用其他名称也可以，不过习惯使用 cls
    * 通过 类名. 调用 类方法，调用方法时，不需要传递 cls 参数
    * 在方法内部
        * 可以通过 cls. 访问类的属性
        * 也可以通过 cls. 调用其他的类方法
    * 语法如下
        ```
        @classmethod
        def 类方法名(cls):
            pass
        ```
* 静态方法
    * 在开发时，如果需要在 类 中封装一个方法，这个方法：
        * 既 不需要 访问 实例属性 或者调用 实例方法
        * 也 不需要 访问 类属性 或者调用 类方法
    * 这个时候，可以把这个方法封装成一个 静态方法
    * 静态方法 需要用 修饰器 @staticmethod 来标识，告诉解释器这是一个静态方法
    * 通过 类名. 调用 静态方法
    * 语法如下
        ```
        @staticmethod
        def 静态方法名():
            pass
        ```

## 2.5 单例设计模式
* 定义一个 类属性，初始值是 None，用于记录 单例对象的引用
* 重写 __new__ 方法
* 如果 类属性 is None，调用父类方法分配空间，并在类属性中记录结果
* 返回 类属性 中记录的 对象引用
```
class MusicPlayer(object):

    # 定义类属性记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 2. 返回类属性的单例引用
        return cls.instance
```
## 2.6 异常
### 2.6.1 捕获异常
* 简单的捕获异常语法
    * 在程序开发中，如果 对某些代码的执行不能确定是否正确，可以增加 try(尝试) 来 捕获异常
    * 捕获异常最简单的语法格式：
    ```
    try:
        尝试执行的代码
    except:
        出现错误的处理
    ```
    * try 尝试，下方编写要尝试代码，不确定是否能够正常执行的代码
    * except 如果不是，下方编写尝试失败的代码
### 2.6.2 错误类型捕获
* 在程序执行时，可能会遇到 不同类型的异常，并且需要 针对不同类型的异常，做出不同的响应，这个时候，就需要捕获错误类型了
* 语法如下：
```
try:
# 尝试执行的代码
    pass
except 错误类型1:
    # 针对错误类型1，对应的代码处理
    pass
except (错误类型2, 错误类型3):
    # 针对错误类型2 和 3，对应的代码处理
    pass
except Exception as result:
    print("未知错误 %s" % result)
```
### 2.6.3 捕获未知错误
```
except Exception as result:
    print("未知错误 %s" % result)
```

### 2.6.4 异常捕获完整语法
```
try:
    # 尝试执行的代码
    pass
except 错误类型1:
    # 针对错误类型1，对应的代码处理
    pass
except 错误类型n:
    # 针对错误类型n，对应的代码处理
    pass
except Exception as result:
    # 打印错误信息
    print(result)
else:
    # 没有异常才会执行的代码
    pass
finally:
    # 无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行的代码")
```


### 2.6.5 抛出 raise 异常

* Python 中提供了一个 Exception 异常类
* 在开发时，如果满足 特定业务需求时，希望 抛出异常，可以：
    * 创建 一个 Exception 的 对象
    * 使用 raise 关键字 抛出 异常对象
```    
def method():
raise Exception(message)
```

## 2.7 模块和包
### 2.7.1 模块
* 模块是 Python 程序架构的一个核心概念
* 每一个以扩展名 py 结尾的 Python 源代码文件都是一个 模块
* 模块名 同样也是一个 标识符，需要符合标识符的命名规则
* 在模块中定义的 全局变量 、函数、类 都是提供给外界直接使用的 工具
* 模块 就好比是 工具包，要想使用这个工具包中的工具，就需要先 导入 这个模块

#### 2.7.1.1 模块的两种导入方式 
1. import 导入
> import 模块名1, 模块名2   
> or  
> import 模块名1   
import 模块名2

* 导入之后
    * 通过 模块名. 使用 模块提供的工具 —— 全局变量、函数、类
* 如果模块的名字太长，可以使用 as 指定模块的名称，以方便在代码中的使用
    > import 模块名1 as 模块别名
     
2. from...import 导入
* 如果希望 从某一个模块 中，导入 部分 工具，就可以使用 from ... import 的方式
* import 模块名 是 一次性 把模块中 所有工具全部导入，并且通过 模块名/别名 访问
> 从 模块 导入 某一个工具  
from 模块名1 import 工具名


* 导入之后
    * 不需要 通过 模块名.
    * 可以直接使用 模块提供的工具 —— 全局变量、函数、类
    
* 如果 两个模块，存在 同名的函数，那么 后导入模块的函数，会 覆盖掉先导入的函数
* 开发时 import 代码应该统一写在 代码的顶部，更容易及时发现冲突
* 一旦发现冲突，可以使用 as 关键字 给其中一个工具起一个别名   

#### 2.7.1.2 模块的搜索顺序
* Python 的解释器在 导入模块 时，会：
    * 搜索 当前目录 指定模块名的文件，如果有就直接导入
    * 如果没有，再搜索 系统目录
* 在开发时，给文件起名，不要和 系统的模块文件 重名
* Python 中每一个模块都有一个内置属性 \_\_file__ 可以 查看模块 的 完整路径

* 原则 —— 每一个文件都应该是可以被导入的
    * 一个 独立的 Python 文件 就是一个 模块
    * 在导入文件时，文件中 所有没有任何缩进的代码 都会被执行一遍

* \_\_name__ 属性
    * \_\_name__ 属性可以做到，测试模块的代码 只在测试情况下被运行，而在 被导入时不会被执行！
    * \_\_name__ 是 Python 的一个内置属性，记录着一个 字符串
    * 如果 是被其他文件导入的，\_\_name__ 就是 模块名
    * 如果 是当前执行的程序 \_\_name__ 是 \_\_main__

### 2.7.2 包
#### 2.7.2.1 概念
* 包 是一个 包含多个模块 的 特殊目录
* 目录下有一个 特殊的文件 \_\_init__.py
* 包名的 命名方式 和变量名一致，小写字母 + _
* 好处：使用 import 包名 可以一次性导入 包 中 所有的模块

#### 2.7.2.2 发布模块
* 制作发布压缩包步骤
    1. 创建 setup.py
    ```
        """
        setup.py 的文件
        有关字典参数的详细信息，可以参阅官方网站：
        https://docs.python.org/2/distutils/apiref.html
        """
        from distutils.core import setup
        setup(name="hm_message",  # 包名
          version="1.0",  # 版本
          description="itheima's 发送和接收消息模块",  # 描述信息
          long_description="完整的发送和接收消息模块",  # 完整描述信息
          author="itheima",  # 作者
          author_email="itheima@itheima.com",  # 作者邮箱
          url="www.itheima.com",  # 主页
          py_modules=["hm_message.send_message",
                      "hm_message.receive_message"])
    ```
    2. 构建模块
    ```
    $ python3 setup.py build
    ```
    3. 生成发布压缩包
    ```
    $ python3 setup.py sdist
    ```
    4. 安装模块
    ```
    $ tar -zxvf hm_message-1.0.tar.gz 
    $ sudo python3 setup.py install
    ```
    5. 卸载模块：直接从安装目录下，把安装模块的 目录 删除就可以
    6. pip 安装第三方模块
        * 第三方模块 通常是指由 知名的第三方团队 开发的 并且被 程序员广泛使用 的 Python 包 / 模块
            * 例如 pygame 就是一套非常成熟的 游戏开发模块
        * pip 是一个现代的，通用的 Python 包管理工具
        * 提供了对 Python 包的查找、下载、安装、卸载等功能
        
        
## 2.8 文件       
### 2.8.1 文件的基本操作
#### 2.8.1.1 操作文件的套路
在 计算机 中要操作文件的套路非常固定，一共包含三个步骤：
1. 打开文件
2. 读、写文件
    * 读 将文件内容读入内存
    * 写 将内存内容写入文件
3. 关闭文件

#### 2.8.1.2 操作文件的函数/方法
* 在 Python 中要操作文件需要记住 1 个函数和 3 个方法

|序号|函数|说明|
|---|---|----|
|01|open|打开文件，并且返回文件操作对象|
|02|read|将文件内容读取到内存|
|03|write|将指定内容写入文件|
|04|close|关闭文件|

* open 函数负责打开文件，并且返回文件对象
* read/write/close 三个方法都需要通过 文件对象 来调用

#### 2.8.1.3 read 方法 —— 读取文件
* open 函数的第一个参数是要打开的文件名（文件名区分大小写）
    * 如果文件 存在，返回 文件操作对象
    * 如果文件 不存在，会 抛出异常
* read 方法可以一次性 读入 并 返回 文件的 所有内容
* close 方法负责 关闭文件
    * 如果 忘记关闭文件，会造成系统资源消耗，而且会影响到后续对文件的访问
* read 方法执行后，会把 文件指针 移动到 文件的末尾
```python
# 1. 打开 - 文件名需要注意大小写
file = open("README")

# 2. 读取
text = file.read()
print(text)

# 3. 关闭
file.close()
```
* 提示:在开发中，通常会先编写 打开 和 关闭 的代码，再编写中间针对文件的 读/写 操作！
* 文件指针
    * 文件指针 标记 从哪个位置开始读取数据
    * 第一次打开 文件时，通常 文件指针会指向文件的开始位置
    * 当执行了 read 方法后，文件指针 会移动到 读取内容的末尾
        * 默认情况下会移动到 文件末尾
* 如果执行了一次 read 方法，读取了所有内容，那么再次调用 read 方法，就获取不到内容。第一次读取之后，文件指针移动到了文件末尾，再次调用不会读取到任何的内容

#### 2.8.1.4 打开文件的方式
* open 函数默认以 只读方式 打开文件，并且返回文件对象
语法如下：
```python
f = open("文件名", "访问方式")
```

|访问方式|说明|
|-------|---|
|r|以只读方式打开文件。文件的指针将会放在文件的开头，这是默认模式。如果文件不存在，抛出异常|
|w|以只写方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件|
|a|以追加方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入|
|r+|以读写方式打开文件。文件的指针将会放在文件的开头。如果文件不存在，抛出异常|
|w+|以读写方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件|
|a+|以读写方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入|

* 频繁的移动文件指针，会影响文件的读写效率，开发中更多的时候会以 只读、只写 的方式来操作文件

写入文件示例
```python
# 打开文件
f = open("README", "w")

f.write("hello python！\n")
f.write("今天天气真好")

# 关闭文件
f.close()
```

#### 2.8.1.5 按行读取文件内容
* read 方法默认会把文件的 所有内容 一次性读取到内存
* 如果文件太大，对内存的占用会非常严重
readline 方法
* readline 方法可以一次读取一行内容
* 方法执行后，会把 文件指针 移动到下一行，准备再次读取

读取大文件的正确姿势
```python
# 打开文件
file = open("README")

while True:
    # 读取一行内容
    text = file.readline()

    # 判断是否读到内容
    if not text:
        break

    # 每读取一行的末尾已经有了一个 `\n`
    print(text, end="")

# 关闭文件
file.close()
```

### 2.8.2 文件/目录的常用管理操作
* 文件或者目录操作都支持 相对路径 和 绝对路径
* 在 终端 / 文件浏览器、 中可以执行常规的 文件 / 目录 管理操作，例如：
    * 创建、重命名、删除、改变路径、查看目录内容、……
* 在 Python 中，如果希望通过程序实现上述功能，需要导入 os 模块
#### 2.8.2.1 文件操作

|序号|方法名|说明|示例|
|---|-----|----|---|
|01|rename|重命名文件|os.rename(源文件名, 目标文件名)|
|02|remove|删除文件|os.remove(文件名)|

#### 2.8.2.2 目录操作

|序号|方法名|说明|示例|
|---|-----|---|----|
|01|listdir|目录列表|os.listdir(目录名)|
|02|mkdir|创建目录|os.mkdir(目录名)|
|03|rmdir|删除目录|os.rmdir(目录名)|
|04|getcwd|获取当前目录|os.getcwd()|
|05|chdir|修改工作目录|os.chdir(目标目录)|
|06|path.isdir|判断是否是文件|os.path.isdir(文件路径)|


### 2.8.3 文本文件的编码格式
* 文本文件存储的内容是基于 字符编码 的文件，常见的编码有 ASCII 编码，UNICODE 编码等
    * Python 2.x 默认使用 ASCII 编码格式
    * Python 3.x 默认使用 UTF-8 编码格式

#### 2.8.3.1 ASCII 编码和 UNICODE 编码
* ASCII 编码
    * 计算机中只有 256 个 ASCII 字符
    * 一个 ASCII 在内存中占用 1 个字节 的空间
    * 8 个 0/1 的排列组合方式一共有 256 种，也就是 2 ** 8
        
* UTF-8 编码格式
    * 计算机中使用 1~6 个字节 来表示一个 UTF-8 字符，涵盖了 地球上几乎所有地区的文字
    * 大多数汉字会使用 3 个字节 表示
    * UTF-8 是 UNICODE 编码的一种编码格式
    
#### 2.8.3.2 Python 2.x 中如何使用中文    
* 在 Python 2.x 文件的 第一行 增加以下代码，解释器会以 utf-8 编码来处理 python 文件
```python
# *-* coding:utf8 *-*
```
这方式是官方推荐使用的！

也可以使用
```python
# coding=utf8
```
unicode 字符串

* 在 Python 2.x 中，即使指定了文件使用 UTF-8 的编码格式，但是在遍历字符串时，仍然会 以字节为单位遍历 字符串
* 要能够 正确的遍历字符串，在定义字符串时，需要 在字符串的引号前，增加一个小写字母 u，告诉解释器这是一个 unicode 字符串（使用 UTF-8 编码格式的字符串）
```python
# *-* coding:utf8 *-*

# 在字符串前，增加一个 `u` 表示这个字符串是一个 utf8 字符串
hello_str = u"你好世界"

print(hello_str)

for c in hello_str:
    print(c)
```    
    
    
## 2.8 eval 函数
* eval() 函数十分强大 —— 将字符串 当成 有效的表达式 来求值 并 返回计算结果
```python
# 基本的数学计算
eval("1 + 1")
#console: 2

# 字符串重复
eval("'*' * 10")
#console: '**********'

# 将字符串转换成列表
type(eval("[1, 2, 3, 4, 5]"))
#console: list

# 将字符串转换成字典
type(eval("{'name': 'xiaoming', 'age': 18}"))
#console: dict
``` 




    


