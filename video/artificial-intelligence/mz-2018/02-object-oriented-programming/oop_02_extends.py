# 继承

class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):
        # 1. 针对子类特有的需求，编写代码
        print("神一样的叫唤...")

        # 2. 使用 super(). 调用原本在父类中封装的方法
        super().bark()

        # 父类名.方法(self) python2.x 时没有super，使用这种方式
        Dog.bark(self)
        # 注意：如果使用子类调用方法，会出现递归调用 - 死循环！
        # XiaoTianQuan.bark(self)

        # 3. 增加其他子类的代码
        print("$%^*%^$%^#%$%")

# 创建一个对象 - 狗对象
wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()




# 创建一个哮天犬的对象
xtq = XiaoTianQuan()

xtq.fly()
xtq.bark()
xtq.eat()

