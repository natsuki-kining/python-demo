# if 语句
age = 20

if age < 20:
    print("是个年轻人")
elif age < 40:
    print("是个中年人")
else:
    print("是个老年人")

# if 嵌套语句

count = 0
if count:
    if count < -1000:
        print("小于一千")
    else:
        print("大于等于一千")
else:
    if count > 1000:
        print("大于一千")
        print("是个整数")
    else:
        print("小于等于一千")
        print("是个整数")

# 随机数 + 逻辑运算
import random
randomNum = random.randint(0,1)
print("randomNum:%s" % randomNum)
if not randomNum:
    print("not randomNum is false")
elif randomNum and age:
    print("randomNum is true")
else:
    print("else random")
