
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a, b = line()
    t = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = line()
        t[x].append(y)
        t[y].append(x)
    
    pare = [-1]*(n+1)
    dist = [0]*(n+1)
    stack = [a]
    while stack:
        v = stack.pop()
        for w in t[v]:
            if w != pare[v]:
                pare[w] = v
                dist[w] = dist[v] + 1
                stack.append(w)
                if w == b:
                    break
    
    ans = (dist[b]+1)//2
    mig = b
    for i in range(ans):
        mig = pare[mig]
    
    pare = [-1]*(n+1)
    dist = [0]*(n+1)
    stack = [mig]
    while stack:
        v = stack.pop()
        for w in t[v]:
            if w != pare[v]:
                pare[w] = v
                dist[w] = dist[v] + 1
                stack.append(w)

    ans += 2*(n-1)
    ans -= max(dist)
    print(ans)