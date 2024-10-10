
def calcSize(v):
    if sizes[v] != -1:
        return sizes[v]
    sizes[v] = 1
    for u in T[v]:
        if sizes[u] == -1:
            parents[u] = v
            sizes[u] = calcSize(u)
            sizes[v] += sizes[u]
    return sizes[v]
    
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    T = [[] for _ in range(n)]

    if n == 0:
        print(0)
        continue

    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        T[u-1] += [v-1]
        T[v-1] += [u-1]

    for i in range(n):
        sizes = [-1]*n
        parents = [-1]*n      
        sizes[i] = calcSize(i)

        stack = [i]
        answer = 0
        while len(stack) > 0:
            e = stack.pop()
            for f in T[e]:
                if parents[f] == e:
                    stack.append(f)
                    answer += sizes[f] * (a[f] ^ a[parents[f]])
        
        print(answer, end = " " if i<n-1 else '\n')