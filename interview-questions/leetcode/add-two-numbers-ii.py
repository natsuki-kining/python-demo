"""
两数相加 II
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。



你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:

输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7

https://leetcode-cn.com/problems/add-two-numbers-ii/

"""

array1 = [7,2,4,3]
array2 = [5,6,4]

from utils.list import *
linkedList = LinkedList()
listNode1 = linkedList.initLinkedList(array1)
listNode2 = linkedList.initLinkedList(array2)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1 = []
        a2 = []
        while l1 or l2:
            if l1:
                a1.append(l1.val)
            else:
                a1.insert(0,0)
            if l2:
                a2.append(l2.val)
            else:
                a2.insert(0,0)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        index = len(a1) - 1

        value = None
        mo = 0
        while index >= 0:
            a_sum = a1[index] + a2[index] + mo
            mo = 0
            if a_sum >= 10:
                mo = 1
                a_sum -= 10

            new = ListNode(a_sum)
            new.next = value
            value = new

            index -= 1

        if mo > 0:
            new = ListNode(mo)
            new.next = value
            value = new
        return value

s = Solution()
v = s.addTwoNumbers(listNode1,listNode2)
v.printNode()
