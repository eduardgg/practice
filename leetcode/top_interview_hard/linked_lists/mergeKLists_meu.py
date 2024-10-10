
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        v = []
        for node in lists:
            while node:
                v.append(node.val)
                node = node.next
        v.sort()
        copia = arrel = ListNode(0)
        for value in v:
            arrel.next = ListNode(value)
            arrel = arrel.next
        return copia.next
        

sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node1.next = node4
node4.next = node6
node2.next = node7
node3.next = node5
node5.next = node8

arrel = sol.mergeKLists([node1, node2, node3])
while arrel:
    print(arrel.val)
    arrel = arrel.next