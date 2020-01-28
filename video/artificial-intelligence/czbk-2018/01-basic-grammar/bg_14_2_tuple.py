# 元组
# 跟list有两点不同，一个是定义，使用（），一个定义好后不能修改里面的元素

# 定义
info_tuple = ("1",2,3,2)

# 统计元组中2的出现次数
print(info_tuple.count(2))

print(info_tuple[1])

print(info_tuple.index("1"))


# 遍历
for object in info_tuple:
    print(object,end="\t")
print()
print("格式化后面的参数就是元素：%s,%s,%s,%s" % info_tuple)