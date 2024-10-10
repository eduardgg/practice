
from sortedcontainers import SortedSet

def check(u):
    # print("checking", u)
    if not u or not posFills[u]: return True
    return posFills[u][0] == pos[u] + 1 and posFills[u][-1] < pos[u] + sizes[u]

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

    posFills = [SortedSet() for _ in range(n+1)]
    bads = set()
    for u in range(1, n+1):
        for v in fills[u]: posFills[u].add(pos[v])
        if not check(u): bads.add(u)

    """print(pare)
    print(fills)
    print(sizes)
    print("perm", p, pos)
    print("posfills:", posFills)
    print("bads", bads)
    print("------------------------")"""

    for _ in range(q):
        x, y = list(map(int, input().split()))

        if p[x] in bads: bads.remove(p[x])
        if p[y] in bads: bads.remove(p[y])
        if pare[p[x]] in bads: bads.remove(pare[p[x]])
        if pare[p[y]] in bads: bads.remove(pare[p[y]])

        if pare[p[x]]: posFills[pare[p[x]]].remove(pos[p[x]])
        if pare[p[y]]: posFills[pare[p[y]]].remove(pos[p[y]])
        if pare[p[x]]: posFills[pare[p[x]]].add(pos[p[y]])
        if pare[p[y]]: posFills[pare[p[y]]].add(pos[p[x]])

        # posFills[p[x]], posFills[p[y]] = posFills[p[y]], posFills[p[x]]
        pos[p[x]], pos[p[y]] = pos[p[y]], pos[p[x]]
        p[x], p[y] = p[y], p[x]

        if not check(p[x]): bads.add(p[x])
        if not check(p[y]): bads.add(p[y])
        if not check(pare[p[x]]): bads.add(pare[p[x]])
        if not check(pare[p[y]]): bads.add(pare[p[y]])

        print("NO" if bads else "YES")
        
        """print("perm", p, pos)
        print("posfills:", posFills)
        print("bads", bads)
        print("------------------------")"""