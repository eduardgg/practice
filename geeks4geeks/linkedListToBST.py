
class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lltobst(ll):
    if len(ll) == 0:
        return None
    val = ll[len(ll)//2]
    n = Node(val)
    n.left = lltobst(ll[:len(ll)//2])
    n.right = lltobst(ll[len(ll)//2+1:])
    return n

ll = [1,2,3,4,5,6,7,8,9,10,11]
head = lltobst(ll)