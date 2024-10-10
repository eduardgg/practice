
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
        while current.left is not None:
            current = current.left
        return current.value

    def maxim(self):
        current = self.root
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
            


def check(u):
    if not u or not posFills[u].root: return True
    return posFills[u].minim() == pos[u] + 1 and posFills[u].maxim() < pos[u] + sizes[u]

for _ in range(int(input())):
    
    n, q = list(map(int, input().split()))
    fills = [[] for _ in range(n+1)]
    pare = [0, 0] + list(map(int, input().split()))
    for i in range(2, n+1):
        fills[pare[i]].append(i)

    p = [-1] + list(map(int, input().split()))
    pos = [-1]*(n+1)
    for i in range(1, n+1):
        pos[p[i]] = i

    sizes = [1]*(n+1)
    dfs, stack = [], [1]
    while stack:
        v = stack.pop()
        for c in fills[v]:
            stack.append(c)
            dfs.append(c)
    while dfs:
        v = dfs.pop()    
        sizes[pare[v]] += sizes[v]

    posFills = [BST() for _ in range(n+1)]
    bads = set()
    for u in range(1, n+1):
        for v in fills[u]: posFills[u].insert(pos[v])
        if not check(u): bads.add(u)

    for _ in range(q):
        x, y = list(map(int, input().split()))

        if p[x] in bads: bads.remove(p[x])
        if p[y] in bads: bads.remove(p[y])
        if pare[p[x]] in bads: bads.remove(pare[p[x]])
        if pare[p[y]] in bads: bads.remove(pare[p[y]])

        if pare[p[x]]: posFills[pare[p[x]]].delete(pos[p[x]])
        if pare[p[y]]: posFills[pare[p[y]]].delete(pos[p[y]])
        if pare[p[x]]: posFills[pare[p[x]]].insert(pos[p[y]])
        if pare[p[y]]: posFills[pare[p[y]]].insert(pos[p[x]])

        pos[p[x]], pos[p[y]] = pos[p[y]], pos[p[x]]
        p[x], p[y] = p[y], p[x]

        if not check(p[x]): bads.add(p[x])
        if not check(p[y]): bads.add(p[y])
        if not check(pare[p[x]]): bads.add(pare[p[x]])
        if not check(pare[p[y]]): bads.add(pare[p[y]])

        print("NO" if bads else "YES")