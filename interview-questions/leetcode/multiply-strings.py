"""
 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

https://leetcode-cn.com/problems/multiply-strings/
"""



num1 = "123"
num2 = "4568"

# 最简单的处理，然而不给用转成整数来处理
class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int (num2))

s1 = Solution1()
print(s1.multiply(num1,num2))


# 突然想起 eval ，最简单的应该是这个
class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(num1 + " * " + num2))

s2 = Solution2()
print(s2.multiply(num1,num2))



# 遍历字符串，获取一个个字符串，转成ASCII码，再转成数字计算，字符转ASCII ord() ,ASCII转字符chr()。字符数字ASCII值比数字大48
class Solution3:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)-1
        l2 = len(num2)-1
        n1 = 0
        n2 = 0
        num = 1
        asciiNum = 48
        while l1 >= 0 or l2 >= 0:
            if l1 >= 0:
                n1 += num * (ord(num1[l1])-asciiNum)
            if l2 >= 0:
                n2 += num * (ord(num2[l2])-asciiNum)
            l1 -= 1
            l2 -= 1
            num *= 10
        return str(n1 * n2)

s3 = Solution3()
print(s3.multiply(num1,num2))

