
# Aquest problema es redueix a un 2SAT, resolt amb Kosaraju's algorithm.
# Aquest codi, usant piles per evitar els errors de recursion depth limit
# de python (que és de només 1000), falla al segon test case...


from collections import defaultdict

def kosaraju(graph):

    visited = set()
    ordre = []
    for node in graph:
        if node not in visited:
            stack = [node]
            while(stack):
                v = stack[-1]
                if v in visited:
                    ordre.append(stack.pop())
                    continue
                visited.add(v)
                for neighbor in graph.get(v, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

    reversed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    
    visited = set()
    components = []
    while ordre:
        node = ordre.pop()
        if node not in visited:
            component = []
            stack = [node]
            while(stack):
                v = stack.pop()
                component.append(v)
                visited.add(v)
                for neighbor in reversed_graph[v]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            components.append(component)

    return components




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
        if i not in g.keys() and i != 0:
            g[i] = []

    comps = kosaraju(g)
    sat = True
    for c in comps:
        vist = set()
        for e in c:
            vist.add(e)
            if -e in vist:
                sat = False
                break
        if not sat:
            break
    
    if sat:
        print("YES")
    else:
        print("NO")