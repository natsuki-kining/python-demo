"""
面试题 16.01. 交换数字
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

示例：

输入: numbers = [1,2]
输出: [2,1]
提示：

numbers.length == 2
https://leetcode-cn.com/problems/swap-numbers-lcci/
"""

numbers = [1,2]

class Solution:
    def swapNumbers(self, numbers):
        return [numbers[1],numbers[0]]


s = Solution()
print(s.swapNumbers(numbers))


class Solution2:
    def swapNumbers(self, numbers):
        numbers[1] = numbers[1] + numbers[0]
        numbers[0] = numbers[1] - numbers[0]
        numbers[1] = numbers[1] - numbers[0]

        return numbers


s2 = Solution2()
print(s2.swapNumbers(numbers))

