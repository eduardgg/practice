# Definition for a binary tree node.
from abc import abstractmethod


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, size=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = size

# Solució lineal, sense definir tamanys:
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            if not r:
                return []
            return inorder(r.left) + [r.val] + inorder(r.right)
        return inorder(root)[k-1]

def findSizes(root):
    num = 1
    if root.left:
        if not root.left.size:
            findSizes(root.left)
        num += root.left.size
    if root.right:
        if not root.right.size:
            findSizes(root.right)
        num += root.right.size
    root.size = num
    return

def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    if root.left:
        if root.left.size == k-1:
            return root.val
        if root.left.size > k-1:
            return kthSmallest(root.left, k)
        return kthSmallest(root.right, k-root.left.size-1)
    if k == 1:
        return root.val
    return kthSmallest(root.right, root.right.size-1)



root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

findSizes(root)
print(root.left.size)
print(kthSmallest(root,3))