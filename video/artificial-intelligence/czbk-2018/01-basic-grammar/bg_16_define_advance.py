"""
交换两个数字
1. 有两个整数变量 `a = 6`, `b = 100`
2. 不使用其他变量，**交换两个变量的值**
"""

a = 6
b = 100

def toSwap():
    global a
    global b
    a = a + b
    b = a - b
    a = a - b

    print("a:%s\nb:%s" %(a,b))

def toSwap2():
    global a
    global b
    a,b = b,a
    # a,b = (b,a)

    print("a:%s\nb:%s" %(a,b))


toSwap2()
