# 变量的基本使用  变量名 = 值

variable1 = 123456789
print(variable1)

variable1 = '1234567890'
print(variable1)

# 变量类型
# 数字型
# 整型 (`int`)
a = 1;
print(type(a))

# 浮点型（`float`）
b = 1.1
print(type(b))

# 布尔型（`bool`）
c = False
d = True
print(type(c))
print(type(d))

#复数型 (`complex`)


# 非数字型
# 字符串
f = "ffff"
print(type(f))

# 列表
g = ["a","b",1,2]
print(type(g))

# 算术运算
# 数字类型直接是可以直接计算，比如int+bool
print(a + c)
print(a + d)

# 字符串拼接
print("a"+"+b")


# 变量的格式化输出
print("格式化字符串%.2f" %121)

format1 = "字符串"
format2 = 12341

print("字符串：%s,数字：%d" %(format1,format2))