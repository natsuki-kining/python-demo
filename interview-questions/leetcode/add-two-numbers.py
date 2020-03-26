"""
两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
https://leetcode-cn.com/problems/add-two-numbers/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

array1 = [2,4,3]
array2 = [5,6,4]

listNode1 = None
for n in array1:
    new = ListNode(n)
    new.next = listNode1
    listNode1 = new

listNode2 = None
for n in array2:
    new = ListNode(n)
    new.next = listNode2
    listNode2 = new


# 方法一、正常思维
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        index = 1

        l1_value = 0
        while l1:
            l1_value += l1.val * index
            index *= 10
            l1 = l1.next

        index = 1
        l2_value = 0
        while l2:
            l2_value += l2.val * index
            index *= 10
            l2 = l2.next

        int_value = l1_value + l2_value
        string_value = str(int_value)

        value = None
        for s in string_value:
            new = ListNode(int(s))
            new.next = value
            value = new

        return value


s = Solution()
s.addTwoNumbers(listNode1,listNode2)



#  方法二，直接节点+节点
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value = None
        remainder = 0
        while l1 and l2:
            val = 0
            sum_value = l1.val + l2.val + remainder
            minus = sum_value - 10
            if (minus >= 0):
                remainder = 1
                val = minus
            else:
                remainder = 0
                val = sum_value
            new = ListNode(val)
            new.next = value
            value = new

            l1 = l1.next
            l2 = l2.next

            #补
            if not l1 and l2:
                l1 = ListNode(0)

            if not l2 and l1:
                l2 = ListNode(0)

        if (remainder > 0):
            new = ListNode(remainder)
            new.next = value
            value = new

        # 反转
        node = ListNode(0)
        while value:
            temp = value.next
            value.next = node.next
            node.next = value
            value = temp
        return node.next

s2 = Solution2()
s2.addTwoNumbers(listNode1,listNode2)