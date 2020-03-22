"""
409. 最长回文串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

https://leetcode-cn.com/problems/longest-palindrome/
"""

"""
执行用时 :
28 ms
, 在所有 Python3 提交中击败了
95.78%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
5.59%
的用户
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        value = 0
        strLen = len(s)
        setArray = set(s[:])

        for i in setArray:
            count = s.count(i)
            if count >= 2:
                value += count // 2 * 2

        if strLen != value:
            value += 1

        return value


charts = "abccccdd"
s = Solution()

value = s.longestPalindrome(charts)

print(value)




# 不借助任何api
class Solution2:
    def longestPalindrome(self, s) -> int:

        dictionary_value = {}
        dictionary_char = {}

        value = 0

        for c in s:
            count = dictionary_char.get(c, 0)
            if (count == 0):
                dictionary_char[c] = 1
            else:
                count += 1
                dictionary_char[c] = count

                ct = count // 2 * 2

                dv = dictionary_value.get(c,0)
                dictionary_value[c] = count

                if dv != 0:
                    value -= (count-1) // 2 * 2

                value += ct

        if len(s) != value:
            value += 1

        return value

s2 = Solution2()
v2 = s2.longestPalindrome(charts)
print(v2)



# 53
class Solution53:
    def longestPalindrome(self, s: str) -> int:
        putout = 0
        for i in set(s[:]):
            times = s.count(i)
            if times % 2 == 0:
                s = s.replace(i, "", times)
                putout += times
            else:
                if not times // 2 == 0:
                    temp_pow = times // 2
                    s = s.replace(i, "", 2 * temp_pow)
                    putout += 2 * temp_pow
        else:
            if len(s) >= 1:
                putout += 1

        return putout


# 官方答案...
import collections
class SolutionAuthority:
    def longestPalindrome_answer(s):
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans