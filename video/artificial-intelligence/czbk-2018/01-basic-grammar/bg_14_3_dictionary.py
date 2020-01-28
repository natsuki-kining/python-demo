# 字典


# 定义 使用 {}

info_dictionary = {
    "sex":"man",
    "age":20,
    "name":"python"
}

# 取值
print(info_dictionary["name"])

# 新增、修改，存在修改，不存在新增
info_dictionary["phone"]="himitsu"

# 删除
info_dictionary.pop("phone")

# 统计键值对数量
print(len(info_dictionary))

# 合并字典
temp_dictionary = {
    "height":1.75
}
info_dictionary.update(temp_dictionary)

# 遍历
for key in info_dictionary:
    print("key:%s,value:%s" %(key,info_dictionary[key]))

# 清空
info_dictionary.clear()
print(info_dictionary)