# while 循环

# 九九乘法表
count1 = 1
count2 = 1
while count1 < 10:
    count2 = count1
    while count2 > 0:
        print("%s * %s = %s" %(count1,count2,count1*count2),end=' \t')
        count2 -= 1

    print("")
    count1+=1
