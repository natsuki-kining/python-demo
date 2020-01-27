# 列表
object_list = [1,2,3,"a","b","c"]

# 遍历
def print_list():
    for object in object_list:
        print(object,end="\t")
    print("")

# 获取指定下标的数据
print(object_list[2])

# 获取指定值的下标
print(object_list.index("b"))

# 修改
print_list();
object_list[1] = "d"
print_list()

# 向列表的末尾追击数据
object_list.append("f")
print_list()

object_list.insert(0,0)
print_list()

# 向末尾追加列表
temp_list = ["F1","F2","F3"]
object_list.extend(temp_list)
print_list()

# 清除
object_list.remove(0)
print_list()
# 最后一个数据删除
object_list.pop()
print_list()

del object_list[0]
print_list()

object_list.clear()
print_list()
