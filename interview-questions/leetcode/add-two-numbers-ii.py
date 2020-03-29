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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printNode(self):
        node = self
        while node != None:
            print(node.val,end="->")
            node = node.next
        print()


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

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1 = []
        a2 = []
        index = 0
        while l1 or l2:
            a1.insert(0, l1.val if l1 else 0)
            a2.insert(0, l2.val if l2 else 0)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            index += 1
        print(a1)
        print(a2)
        index = len(a1) - 1

        head = ListNode(0)
        h = head
        mo = 0
        while index >= 0:
            a_sum = a1[index] + a2[index] + mo
            mo = 0
            if a_sum >= 10:
                mo = a_sum % 10 + 1
                a_sum -= 10

            new = ListNode(a_sum)
            h.next = new
            h = new
            index -= 1
        return head.next

s = Solution()
v = s.addTwoNumbers(listNode1,listNode2)
v.printNode()


class Solution2:
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

s2 = Solution2()
v2 = s2.addTwoNumbers(listNode1,listNode2)
v2.printNode()


# emmmmm 链表的初始化错了，导致pycharm跟LeetCode执行的结果不一样、pycharm第一个正确，LeetCode第二个正确