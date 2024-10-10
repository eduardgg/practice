class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def vecToLL(v):
    root = ListNode()
    copy = root
    for i in v[0:len(v)-1]:
        copy.val = i
        copy.next = ListNode()
        copy = copy.next
    if len(v) > 0:
        copy.val = v.pop()
    return root

def printLL(l):
    while l:
        print(l.val, end=" ")
        l = l.next
    print()

def addNums(l1, l2):
    l = ListNode()
    root = l
    res = 0
    while l1 or l2:
        op = res
        if l1:
            op += l1.val
            l1 = l1.next
        if l2:
            op += l2.val
            l2 = l2.next
        l.val = op % 10
        res = op // 10
        if l1 or l2:
            l.next = ListNode()
            l = l.next
    if res > 0:
        l.next = ListNode(res)
    return root

def oddEvenLinkedList(l):
    oddll = ListNode()
    oddRoot = oddll
    evenll = ListNode()
    evenRoot = evenll
    if not l or not l.next:
        return l
    oddll.val = l.val
    l = l.next
    evenll.val = l.val
    l = l.next
    i = 3
    while l:
        if i % 2 != 0:
            oddll.next = ListNode(l.val)
            oddll = oddll.next
        else:
            evenll.next = ListNode(l.val)
            evenll = evenll.next
        l = l.next
        i += 1
    oddll.next = evenRoot
    return oddRoot

def getIntersectionNode(headA, headB):
    va = []
    llA = headA
    while llA:
        va.append(llA)
        llA = llA.next
    vb = []
    llB = headB
    while llB:
        vb.append(llB)
        llB = llB.next
    if len(va) == 0 or len(vb) == 0:
        return None
    ultimA = va.pop()
    ultimB = vb.pop()
    if ultimA != ultimB:
        return None
    while ultimA == ultimB:
        if len(va) == 0 or len(vb) == 0:
            return ultimA
        ultimA = va.pop()
        ultimB = vb.pop()
    return ultimA.next

headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = headA.next.next
intersection = getIntersectionNode(headA, headB)
print(intersection.val)
printLL(intersection)

"""
# Samples for addNums
l1 = vecToLL([9,9,9,9,9,9,9])
l2 = vecToLL([9,9,9,9])
l = addNums(l1, l2)
printLL(l1)
printLL(l2)
printLL(l)
l1 = vecToLL([2,4,3])
l2 = vecToLL([5,6,4])
l = addNums(l1, l2)
printLL(l1)
printLL(l2)
printLL(l)
"""

"""
# Samples for oddEvenLinkedList:
l = vecToLL([])
printLL(oddEvenLinkedList(l))
l = vecToLL([1])
printLL(oddEvenLinkedList(l))
l = vecToLL([1,2])
printLL(oddEvenLinkedList(l))
l = vecToLL([1,2,3])
printLL(oddEvenLinkedList(l))
l = vecToLL([1,2,3,4,5,6,7,8,9,10])
printLL(oddEvenLinkedList(l))
"""