class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def doInorder(root, sol):
    if root and root.val:
        doInorder(root.left, sol)
        sol.append(root.val)
        doInorder(root.right, sol)

def vecToTree(tree):
    root = Node(tree[0])
    queue = [root]
    pos = 1
    while len(queue) > 0:
        n = queue.pop(0)
        if pos < len(tree):
            n.left = Node(tree[pos])
            if tree[pos]:
                queue += [n.left]
        if pos+1 < len(tree) and tree[pos+1]:
            n.right = Node(tree[pos+1])
            if tree[pos+1]:
                queue += [n.right]
        pos += 2
    solution = []
    doInorder(root, solution)
    return solution


tree = [1, None, 2, 3]
print(vecToTree(tree))

tree = [1, 2, 3, 4, 5]
print(vecToTree(tree))

tree = [1, 2, 3, 4, None, None, 5, 6, 7, 8, None, 9]
print(vecToTree(tree))