class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printNode(self):
        node = self
        while node != None:
            sign = ""
            if node.next:
                sign = "->"
            print(node.val,end=sign)
            node = node.next
        print()


class LinkedList:
    @staticmethod
    def init(array):
        list_node = ListNode(0)
        l1 = list_node
        for n in array:
            new = ListNode(n)
            l1.next = new
            l1 = new
        return list_node.next