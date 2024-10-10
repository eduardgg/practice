# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTreeVector(root):
    queue = [root]
    output = []
    while len(queue) > 0:
        l = len(queue)
        for i in range(l):
            n = queue.pop(0)
            if n:
                output.append(n.val)
                queue.append(n.left)
                queue.append(n.right)
            else:
                output.append(None)
        j = 0
        while output[len(output)-1-j] == None:
            j += 1
    print(output[0:len(output)-j])

def constructTree(root, preorder, inorder):
    root.val = preorder[0]
    pos = 0
    while True:
        if inorder[pos] == root.val:
            break
        pos += 1
    if pos > 0:
        root.left = TreeNode()
        constructTree(root.left, preorder[1:pos+1], inorder[0:pos])
    if pos < len(inorder)-1:
        root.right = TreeNode()
        constructTree(root.right, preorder[pos+1:], inorder[pos+1:])

# Define the binary tree
root = TreeNode()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
constructTree(root, preorder, inorder)
printTreeVector(root)
"""print(root.val, end = ", ")
print(root.left.val, end = ", ")
print(root.right.val, end = ", ")
print(root.right.left.val, end = ", ")
print(root.right.right.val)"""