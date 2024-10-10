
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)
        # Si el valor ja existeix, no fem res

    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def minim(self):
        current = self.root
        if not current:
            return None
        while current.left is not None:
            current = current.left
        return current.value

    def maxim(self):
        current = self.root
        if not current:
            return None
        while current.right is not None:
            current = current.right
        return current.value
    
    def _delete_recursively(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            # Cas en què trobem el node a eliminar
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node amb dos fills: troba el mínim del subarbre dret
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursively(node.right, min_node.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_recursively(self.root, [])

    def _inorder_recursively(self, node, result):
        if node is not None:
            self._inorder_recursively(node.left, result)
            result.append(node.value)
            self._inorder_recursively(node.right, result)
        return result
    
    def first_greater(self, value):
        return self.first_greater_recursively(self.root, value)

    def first_greater_recursively(self, node, value):
        if node is None:
            return None

        if node.value == value:
            return node.value
        elif node.value < value:
            return self.first_greater_recursively(node.right, value)
        else:
            left_result = self.first_greater_recursively(node.left, value)
            if left_result is not None:
                return left_result
            else:
                return node.value
    
    def first_less(self, value):
        return self.first_less_recursively(self.root, value)

    def first_less_recursively(self, node, value):
        if node is None:
            return None

        if node.value == value:
            return node.value
        elif node.value > value:
            return self.first_less_recursively(node.left, value)
        else:
            left_result = self.first_less_recursively(node.right, value)
            if left_result is not None:
                return left_result
            else:
                return node.value
            
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, q = line()
    a = line()
    s = sum(a)
    bst = BST()

    for i in range(n):
        if a[i] == 1:
            bst.insert(i)

    for _ in range(q):
        b = line()
        if b[0] == 1:
            # Query
            if s < b[1]:
                print("NO")
            elif (s - b[1])%2 == 0:
                print("YES")
            elif bst.minim() != None and b[1] <= s - 2*min(bst.minim(), n-1-bst.maxim()):
                print("YES")
            else:
                print("NO")
        else:
            i = b[1]-1
            if a[i] != b[2]:
                # Hi ha canvi
                s += b[2] - a[i]
                a[i] = b[2]
                if b[2] == 1:
                    bst.insert(i)
                else:
                    bst.delete(i)