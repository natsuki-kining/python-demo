# 私有属性
class Test:
    def __init__(self,flag):
        self.__count = 1 # 私有属性
        self.flag = flag

    def __private_method(self):
        print("私有方法")

    def __str__(self):
        return ("count:%s,flag:%s" %(self.__count,self.flag))


test = Test("flag")
print(test)
print(test.__count)