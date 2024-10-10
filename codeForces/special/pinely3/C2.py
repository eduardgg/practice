class BLLNode(object):
    def __init__(self, val=None, pre=None, nex=None):
        self.val = val
        self.pre = pre
        self.nex = nex

def vecToBLL(v):
    root = BLLNode()
    copy = root
    for i in v[0:len(v)-1]:
        copy.val = i
        copy.nex = BLLNode()
        prev = copy
        copy = copy.nex
        copy.pre = prev
    if len(v) > 0:
        copy.val = v[-1]
    return root

def deleteNode(n):
    if n.pre and n.nex:
        (n.pre).nex = n.nex
        (n.nex).pre = n.pre
        n = n.pre
    elif n.pre:
        (n.pre).nex = None
        n = n.pre
    elif n.nex:
        (n.nex).pre = None
        n = n.nex

def printBLL(l):
    while True:
        if l.pre == None:
            break
        l = l.pre
    while l:
        print(l.val, end=" ")
        l = l.nex
    print()



t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    l.sort()
    r.sort()
    ints = []
    
    """
    # VERSIÓ INEFICIENT:
    # (ja que usa el pop() de posicions concretes en vectors)
    posl = 0
    for i in range(len(r)):
        if posl < len(l) and l[posl] >= r[i]:
            posl -= 1
        while posl < len(l) and l[posl] < r[i]:
            posl += 1
        posl -= 1
        ints += [r[i] - l.pop(posl)]
    """

    # VERSIÓ EFICIENT:
    # (Usa una estructura de dades generada per ser eficient a l'eliminar
    # posicions concretes d'un vector, a través d'una "bi"-linked list)
    bll = vecToBLL(l)
    for i in range(len(r)):
        while bll.nex and bll.nex.val < r[i]:
            bll = bll.nex
        ints += [r[i] - bll.val]
        deleteNode(bll)

    # Fragment comú:
    ints.sort()
    c.sort()
    cost = 0
    for i in range(len(c)):
        cost += c[i]*ints[-1-i]
    print(cost)