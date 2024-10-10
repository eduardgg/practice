
def find(u):
    if leader[u] == u:
        return u
    leader[u] = find(leader[u])
    return leader[u]

def union(a, b):
    la = leader[a]
    lb = leader[b]
    if rank[la] > rank[lb]:
        leader[lb] = la
    elif rank[la] < rank[lb]:
        leader[la] = lb
    else:
        leader[lb] = la
        rank[la] += 1
    return

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    leader = [i for i in range(n)]
    rank = [1]*(n)
    print("YES")
    ans = []
    for i in range(n-1, 0, -1):
        res = [-1]*i
        for u in range(n):
            v = res[a[u]%i]
            if v == -1:
                res[a[u]%i] = u
            elif find(u) != find(v):
                union(u, v)
                ans.append((u, v))
                break
    for (u, v) in ans[::-1]:
        print(u+1, v+1)
        