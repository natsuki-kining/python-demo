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


class LinkedList:
    def initLinkedList(self,array):
        listNode = ListNode(0)
        l1 = listNode
        for n in array:
            new = ListNode(n)
            l1.next = new
            l1 = new
        return listNode.next