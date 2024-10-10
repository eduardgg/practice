# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    queue = [root]
    ordre = True
    solution = []
    while len(queue) > 0:
        l = len(queue)
        v = []
        for i in range(l):
            n = queue.pop(0)
            if not n:
                continue
            if n.val or n.val==0:
                v.append(n.val)
            queue += [n.left]
            queue += [n.right]
        if ordre == False:
            v.reverse()
        if len(v) > 0:
            solution.append(v)
        ordre = not ordre
    return solution

# Define the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(zigzagLevelOrder(root))