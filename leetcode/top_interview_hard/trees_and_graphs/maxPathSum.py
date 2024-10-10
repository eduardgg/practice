
# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        # Afegit per mi:
        self.maxPath = None
            # Puntuació màxima dels camins que passen estrictament pel
            # node "self" i a més aquest és el punt més alt del camí.
        self.valEsq = None
            # Puntuació del camí més llarg que acaba a self.left
        self.valDre = None
            # Puntuació del camí més llarg que acaba a self.right

class Solution(object):
    def maxPathSum(self, root):

        def findMaxPaths(node):
            # Això troba el maxPath de node, a través de la crida
            # recursiva de tots els nodes inferiors, trobant-los així
            # tots, i podent fer el màxim per acabar el problema. El
            # codi calcula bé els valors encara que sigui una fulla.  

            # Trobem el valor del camí de l'esquerra del node:
            node.valEsq = 0
            if node.left:
                findMaxPaths(node.left)
                node.valEsq += max(
                    0,
                    node.left.val,
                    node.left.val + node.left.valEsq,
                    node.left.val + node.left.valDre
                )
            
            # Trobem el valor del camí de la dreta del node:
            node.valDre = 0
            if node.right:
                findMaxPaths(node.right)
                node.valDre += max(
                    0,
                    node.right.val,
                    node.right.val + node.right.valEsq,
                    node.right.val + node.right.valDre
                )

            # Trobem el valor del camí màxim amb alçada fins el node:
            node.maxPath = node.val + max(0, node.valEsq) + max(0, node.valDre)
            return

        """
        # Trobem els pares de cada node:
        # (no cal per aquest problema)
        stack = [root]
        while len(stack) > 0:
            r = stack.pop()
            if r.left:
                r.left.parent = r
                stack.append(r.left)
            if r.right:
                r.right.parent = r
                stack.append(r.right)
        """
        
        findMaxPaths(root)
        
        stack = [root]
        maxim = root.val
        while len(stack) > 0:
            r = stack.pop()
            if r.maxPath > maxim:
                maxim = r.maxPath
            if r.left:
                stack.append(r.left)
            if r.right:
                stack.append(r.right)
        return maxim
            

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
maxim = sol.maxPathSum(root)

print("Solucions:")
print(root.maxPath)
print(root.left.maxPath)
print(root.right.maxPath)
print(root.right.left.maxPath)
print(root.right.right.maxPath)
print("Màxim: " + str(maxim))