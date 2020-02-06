# 七 高级语法

## 7.1 GIL（全局解释器锁）

## 7.2 深拷贝、浅拷贝

### 7.2.1 浅拷贝
> 浅拷贝是对于一个对象的顶层拷贝,拷贝了引用，并没有拷贝内容

### 7.2.2 深拷贝
> 深拷贝是对于一个对象所有层次的拷贝(递归)

## 7.3 私有化
* xx: 公有变量
* \_x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
* \_\_xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
* \_\_xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:\_\_init__ , __ 不要自己发明这样的名字
* xx_:单后置下划线,用于避免与Python关键词的冲突
* 父类中属性名为__名字的，子类不继承，子类不能访问
* 如果在子类中向__名字赋值，那么会在子类中定义的一个与父类相同名字的属性
* _名的变量、函数、类在使用from xxx import *时都不会被导入

## 7.4 import导入模块

### 7.4.1 import 搜索路径
```python
import sys
print(sys.path)
```
* 从上面列出的目录里依次查找要导入的模块文件
* '' 表示当前路径
* 列表中的路径的先后顺序代表了python解释器在搜索模块时的先后顺序
```python
# 程序执行时添加新的模块路径
import sys
sys.path.append('/home/itcast/xxx')
sys.path.insert(0, '/home/itcast/xxx')  # 可以确保先搜索这个路径
print(sys.path.insert(0,"/home/python/xxxx"))
print(sys.path)
```


### 7.4.2 重新导入模块
> import导入模块只会导入一次，因此即使模块进行了修改，import也不会重新导入，这时候需要使用reload重新导入

```python
import module

from imp import reload
reload(module)
```






