
# Aquest problema es redueix a un 2SAT, resolt amb Kosaraju's algorithm.
# Aquest codi, usant recursió (perill de recursion depth limit), falla
# per time limit al test case #3.


def kosaraju(graph):

    def dfs_first_pass(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_first_pass(neighbor)
        stack.append(node)

    def dfs_second_pass(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in visited:
                dfs_second_pass(neighbor, component)

    visited = set()
    stack = []
    reversed_graph = dict()

    # Primera passada per omplir la pila en l'ordre correcte
    for node in graph:
        if node not in visited:
            dfs_first_pass(node)

    # Inverteix les arestes del graf
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor] = reversed_graph.get(neighbor, []) + [node]

    visited = set()
    components = []

    # Segona passada per identificar les CFC
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_second_pass(node, component)
            components.append(component)

    return components


# Aquest problema es redueix a un 2SAT, resolt amb Kosaraju's algorithm

from collections import defaultdict

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(3):
        a.append(line())
    
    gaux = defaultdict(set)
    for i in range(n):
        for j in range(3):
            if -a[j][i] != a[(j+1)%3][i]:
                gaux[-a[j][i]].add(a[(j+1)%3][i])
            if -a[j][i] != a[(j+2)%3][i]:
                gaux[-a[j][i]].add(a[(j+2)%3][i])
    
    g = {i: list(gaux[i]) for i in gaux.keys()}
    for i in range(-n, n+1):
        if i not in g.keys():
            g[i] = []
    # print(g)

    sat = True
    comps = kosaraju(g)
    for c in comps:
        vist = set()
        for e in c:
            if -e in vist:
                sat = False
                break
            elif e not in vist:
                vist.add(e)
        if not sat:
            break
    
    if sat:
        print("YES")
    else:
        print("NO")