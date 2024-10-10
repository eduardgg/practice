
# Funciona per C2, falla a C1 degut al recursion depth.
# Time Limit Exceeded degut a les condicions de C3.

def win1(r):
    ok = False
    for w in g[r]:
        if win(w, r):
            ok = True
            break
    return ok

def win(w, u):
    if (w, u) not in dp.keys():
        if len(g[w]) == 1:
            dp[(w, u)] = True
        else:
            ok = True
            for v in g[w]:
                if v != u and win(v, w):
                    ok = False
                    break
            dp[(w, u)] = ok
    return dp[(w, u)]


n, t = list(map(int, input().split()))
g = [[] for _ in range(n+1)]
dp = {}
for i in range(n-1):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

rounds = list(map(int, input().split()))
for r in rounds:
    if win1(r):
        print("Ron")
    else:
        print("Hermione")