class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
"""def doInorder(root, sol):
    if root and root.val:
        doInorder(root.left, sol)
        sol.append(root.val)
        doInorder(root.right, sol)"""

def zigzag(tree):
    if len(tree) == 0:
        return []
    root = Node(tree[0])
    queue = [root]
    pos = 1
    ordre = True
    solution = []
    while len(queue) > 0:
        l = len(queue)
        v = []
        for i in range(l):
            n = queue.pop(0)
            v.append(n.val)
            if pos < len(tree):
                n.left = Node(tree[pos])
                if tree[pos]:
                    queue += [n.left]
            if pos+1 < len(tree) and tree[pos+1]:
                n.right = Node(tree[pos+1])
                if tree[pos+1]:
                    queue += [n.right]
            pos += 2
        if ordre == False:
            v.reverse()
        solution.append(v)
        ordre = not ordre
    return solution


tree = [1, None, 2, 3]
print(zigzag(tree))

tree = [1, 2, 3, 4, 5]
print(zigzag(tree))

tree = [1, 2, 3, 4, None, None, 5, 6, 7, 8, None, 9]
print(zigzag(tree))

tree = [3,9,20,None,None,15,7]
print(zigzag(tree))

tree = [1]
print(zigzag(tree))

tree = []
print(zigzag(tree))

tree = [1,2,3,4,None,None,5]
print(zigzag(tree))

tree = [0,2,4,1,None,3,-1,5,1,None,6,None,8]
print(zigzag(tree))