
import sys

sys.setrecursionlimit(10**6)

class Graph:

    def __init__(self, n):
        self.V = n
        self.graph = [[] for _ in range(n)]
        self.indegree = [0] * n
        self.outdegree = [0] * n

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.outdegree[u] += 1
        self.indegree[v] += 1

    def has_eulerian_path(self):
        start_nodes = 0
        end_nodes = 0

        for i in range(self.V):
            out_d = self.outdegree[i]
            in_d = self.indegree[i]

            if out_d - in_d == 1:
                start_nodes += 1
            elif in_d - out_d == 1:
                end_nodes += 1
            elif in_d != out_d:
                return False

        # Comprovem les condicions per un camí eulerià:
        return (start_nodes == 1 and end_nodes == 1) or (start_nodes == 0 and end_nodes == 0)

    def dfs(self, u, path):
        # Recorrem les arestes del vèrtex u:
        for v in self.graph[u]:
            if (u, v) in self.visited_edges:
                continue
            self.visited_edges.add((u, v))
            self.dfs(v, path)
        path.append(u)

    def eulerian_path(self):
        if not self.has_eulerian_path():
            return None

        # Trobem el vèrtex d'inici:
        start = 0
        for i in range(self.V):
            if self.outdegree[i] - self.indegree[i] == 1:
                start = i
                break

        self.visited_edges = set()
        path = []
        self.dfs(start, path)

        return path[::-1]



# De Bruijn Sequence:

n = int(input())

if n == 1:
    print("01")
else:
    g = Graph(1 << (n-1))
    for i in range(1 << (n-1)):
        g.add_edge(i, ((i & ((1 << (n-2)) - 1)) << 1))
        g.add_edge(i, ((i & ((1 << (n-2)) - 1)) << 1) + 1)

    ep = g.eulerian_path()
    result = '0'*n + ''.join([str(ep[i] % 2) for i in range(2, len(ep))])
    print(result)
    