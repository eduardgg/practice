# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    def doInorder(r, sol):
        if r and r.val:
            doInorder(r.left, sol)
            sol.append(r.val)
            doInorder(r.right, sol)
    solution = []
    doInorder(root, solution)
    return solution

# Define the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(inorderTraversal(root))