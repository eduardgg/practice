
# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def serialize(self, root):
        queue = [root]
        serie = []
        while len(queue) > 0:
            r = queue.pop(0)
            if not r:
                serie += [None]
                continue
            serie += [r.val]
            if r.left:
                queue.append(r.left)
            else:
                queue.append(None)
            if r.right:
                queue.append(r.right)
            else:
                queue.append(None)
        i = 0
        l = len(serie)
        while serie[l-1-i] == None:
            i += 1
        return serie[:l-i]

    def deserialize(self, data):
        value = data.pop(0)
        root = TreeNode(value)
        queue = [root]
        while len(data) > 0:
            r = queue.pop(0)
            rleft = data.pop(0)
            if rleft or rleft == 0:
                r.left = TreeNode(rleft)
                queue += [r.left]
            rright = data.pop(0)
            if rright or rright == 0:
                r.right = TreeNode(rright)
                queue += [r.right]
        return root

    def lowestCommonAncestor(self, root, p, q):
        
        # Aquí, p i q són els valors dels nodes

        pares = {root.val:None}
        stack = [root]
        while len(stack) > 0:
            r = stack.pop()
            if r.right:
                stack.append(r.right)
                pares[r.right.val] = r.val
            if r.left:
                stack.append(r.left)
                pares[r.left.val] = r.val
        
        paresP = []
        while p or p == 0:
            paresP += [p]
            p = pares[p]
            
        paresQ = []
        while q or q == 0:
            paresQ += [q]
            q = pares[q]

        while True:
            ap = paresP.pop()
            aq = paresQ.pop()
            if ap != aq:
                return last
            last = ap

    def lowestCommonAncestor2(self, root, p, q):
        
        # Aquí, p i q són de tipus TreeNode()
        # L'output també és el node corresponent

        pares = {root:None}
        stack = [root]
        while len(stack) > 0:
            r = stack.pop()
            if r.right:
                stack.append(r.right)
                pares[r.right] = r
            if r.left:
                stack.append(r.left)
                pares[r.left] = r
        
        paresP = []
        while p:
            paresP += [p]
            p = pares[p]
            
        paresQ = []
        while q:
            paresQ += [q]
            q = pares[q]

        # print([i.val for i in paresP])
        # print([i.val for i in paresQ])

        while min(len(paresP),len(paresQ)) > 0:
            ap = paresP.pop()
            aq = paresQ.pop()
            if ap != aq:
                return last
            last = ap
        return last
    
ser = Solution()

"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
ans = ser.serialize(root)
print(ans)

data = [3,5,1,6,2,0,8,None,None,7,4]
ans = ser.deserialize(data)
print(ans.val)
print(ans.left.val)
print(ans.left.left.val)
print(ans.left.right.val)
print(ans.left.right.left.val)
print(ans.left.right.right.val)
print(ans.right.val)
print(ans.right.left.val)
print(ans.right.right.val)
"""

data = [3,5,1,6,2,0,8,None,None,7,4]
p, q = 4, 6
root = ser.deserialize(data)
ans = ser.lowestCommonAncestor(root, p, q)
print(ans)

data = [3,5,1,6,2,0,8,None,None,7,4]
root = ser.deserialize(data)
p = root.left.right.right
q = root.left
ans = ser.lowestCommonAncestor2(root, p, q)
print(ans.val)