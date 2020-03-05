# 合并排序的数组
# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
# 初始化 A 和 B 的元素数量分别为 m 和 n。
#

# 输入:
# A = [1,2,3,0,0,0], m = 3
# B = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]
# https://leetcode-cn.com/problems/sorted-merge-lcci/


# 谜之跪了...
A = [1, 2, 3, 0, 0, 0]
m = 3
B = [2, 5, 6]
n = 3


A = A[:m]
A.extend(B)
A.sort()
print(A)

# 运行结果理论上是对的啊
# 但是判定非说我的输出是 [1,2,3,0,0,0]
# 难道是版本的问题之类的吗?
# 很迷...


A_2 = [1, 2, 3, 0, 0, 0]
m_2 = 3
B_2 = [2, 5, 6]
n_2 = 3
# 官方答案倒是更简单 两行
# 从运行效果来看我也不知道我错哪了...
A_2[m:] = B_2
A_2.sort()
print(A_2)


A_3 = [1, 2, 3, 0, 0, 0]
m_3 = 3
B_3 = [2, 5, 6]
n_3 = 3

class Solution:
    def merge(self, A: [int], m: int, B: [int], n: int):
        A = A[:m]
        A.extend(B)
        A.sort()
        return A

s = Solution();
C_3 = s.merge(A_3,m_3,B_3,n_3)

print(A_3)
print(C_3)