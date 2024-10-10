
# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        stack = [root]
        serie = []
        while len(stack) > 0:
            a = stack.pop()
            if a == ".":
                serie.append(".")
                continue
            serie.append(a.val)
            if a.right and a.right.val:
                stack.append(a.right)
            else:
                stack.append(".")
            if a.left and a.left.val:
                stack.append(a.left)
            else:
                stack.append(".")
        return serie
        """
        # Per retornar una string, canviem la línia anterior per:
        return ' '.join(str(e) for e in serie)
        """
        
    def deserialize(self, data):
        """
        # Afegim aquest paràgraf perquè LeetCode vol un string
        # (En la meva versió,simplement l'eliminem)
        datanou = []
        for i in data.split():
            if i == ".":
                datanou.append(i)
                continue
            datanou.append(int(i))
        data = datanou
        """
        root = TreeNode()
        stack = [root]
        while len(stack) > 0:
            actual = stack.pop()
            value = data.pop(0)
            if value == '.':
                actual = None
                continue
            actual.val = value
            actual.right = TreeNode()
            actual.left = TreeNode()
            stack.append(actual.right)
            stack.append(actual.left)
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

ser = Codec()
deser = Codec()
ans = ser.serialize(root)
print(ans)
arrel = deser.deserialize(ans)
ans2 = ser.serialize(arrel)
print(ans2)

"""print(arrel.val)
print(arrel.left.val)
print(arrel.left.left.val)
print(arrel.left.right.val)
print(arrel.right.val)
print(arrel.right.left.val)
print(arrel.right.left.left.val)
print(arrel.right.left.right.val)
print(arrel.right.right.val)
print(arrel.right.right.left.val)
print(arrel.right.right.right.val)"""