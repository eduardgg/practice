# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        v = []
        while head:
            v.append(head.val)
            head = head.next
        v.sort()
        copia = arrel = ListNode(0)
        for i in range(len(v)):
            arrel.next = ListNode(v[i])
            arrel = arrel.next
        return copia.next
        
sol = Solution()
node1 = ListNode(-1)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(0)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

arrel = sol.sortList(node1)
while arrel:
    print(arrel.val)
    arrel = arrel.next