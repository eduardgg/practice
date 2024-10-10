
class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sortedList(node):
    if node == None:
        return []
    else:
        return sortedList(node.left) + [node.value] + sortedList(node.right)

def mergeBST(node1, node2):
    v1 = sortedList(node1)
    v2 = sortedList(node2)
    v = []
    i, j = 0, 0
    while i < len(v1) or j < len(v2):
        if i == len(v1) or v2[j] <= v1[i]:
            v.append(v2[j])
            j += 1
        elif j == len(v2) or v1[i] <= v2[j]:
            v.append(v1[i])
            i += 1
    return v


root1 = Node(5)
root1.left = Node(3)
root1.right = Node(6)
root1.left.left = Node(2)
root1.left.right = Node(4)

root2 = Node(2)
root2.left = Node(1)
root2.right = Node(3)
root2.right.right = Node(7)
root2.right.right.left = Node(6)

print(sortedList(root1))
print(sortedList(root2))
print(mergeBST(root1, root2))