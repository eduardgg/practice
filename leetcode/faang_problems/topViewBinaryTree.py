# Given a binary tree, print the top view
# És a dir, en ordre d'esquerra a dreta, imprimir el
# node que hi hagi més amunt en l'arbre binari.
# Ens basarem en un BFS ja que, a més altura, més prioritat.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

"""root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
root.left.right.left = Node(7)"""

pos = 0
min = 0
max = 0
queue = [[root,0]]
leftv = []
rightv = []

while len(queue) > 0:
    arrel, pos = queue.pop(0)
    if arrel:
        if pos < min:
            leftv += [arrel.val]
            min = pos
        if pos > max:
            rightv += [arrel.val]
            max = pos
        if arrel.left:
            queue.append([arrel.left, pos-1]) 
        if arrel.right:
            queue.append([arrel.right, pos+1])

print(leftv[::-1] + [root.val] + rightv)