
import random

tc = int(input())
for i in range(tc):

    n = int(input())
    t = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        t[u].append(v)
        t[v].append(u)
    
    stack = [1]
    dfs = []
    parent = [-1]*(n+1)
    parent[1] = 1
    height = [1]*(n+1)
    # size = [1]*(n+1)
    while stack:
        v = stack.pop()
        for u in t[v]:
            if u != parent[v]:
                parent[u] = v
                stack.append(u)
                dfs.append(u)
    fulla = dfs[-1]
    while dfs:
        u = dfs.pop()
        # size[parent[u]] += size[u]
        height[parent[u]] = max(height[parent[u]], height[u] + 1)
    leaves = {l for l in range(1, n+1) if height[l] == 1}

    # Cas Trivial:
    mh = max(height)
    if mh <= 160:
        print("?", fulla, flush=True)
        if input() == "0":
            for _ in range(mh-2):
                print("?", fulla, flush=True)
                suda = input()
            print("!", 1, flush=True)
        else:
            print("!", fulla, flush=True)
        continue

    q = 160
    lider = 1
    left = {i+1 for i in range(n)}
    par = True

    while q:
        if len(left) == 1:
            print("!", left.pop(), flush=True)
            break
        if par:
            u = list(left)[random.randint(0, len(left)-1)]
            print("?", u, flush=True)
            if input() == "0":
                lider = parent[lider]
                left.add(lider)
                dfs = [u]
                while dfs:
                    v = dfs.pop()
                    if v in left:
                        left.remove(v)
                        if v in leaves:
                            leaves.remove(v)
                        for w in t[v]:
                            if w != parent[v]:
                                dfs.append(w)
                for l in leaves:
                    if l in left:
                        left.remove(l)
                leaves = {parent[l] for l in leaves}
                for l in leaves:
                    left.add(l)
                leaves.add(parent[u])
            else:
                lider = u
                new = {u}
                stack = [u]
                while stack:
                    v = stack.pop()
                    for w in t[v]:
                        if w in left and w != parent[v]:
                            stack.append(w)
                            new.add(w)
                left = {f for f in new}
            par = False
        else:
            print("?", lider, flush=True)
            if input() == "0":
                print("!", parent[lider], flush=True)
                break
            par = True
        q -= 1