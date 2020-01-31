class Cat:
    """这是一个猫类"""


    def __init__(self):
        print("初始化方法")

    def __str__(self):
        return "str方法"+self.name

    def __del__(self):
        print("del "+self.name)

    def eat(self):
        print("%s小猫爱吃鱼" %self.name)

    def drink(self):
        print("%s小猫在喝水" %self.name)

tom = Cat()
tom.name = "tom"
tom.drink()
tom.eat()

print(tom)

print("%d" %id(tom))
print("%x" %id(tom))


vom = Cat()
vom.name = "vom"
vom.drink()
vom.eat()