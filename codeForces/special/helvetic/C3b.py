
# DP iterativa, no recursiva (funciona per arbres línia, com C1).
# Segueix fallant per Time Limit Exceeded amb les condicions de C3.

def win(w, u):
    if (w, u) not in dp.keys():
        stack = [(w, u)]
        while stack:
            v2, v1 = stack[-1]
            ok = True
            inv = False
            for v3 in g[v2]:
                if v3 != v1:
                    if (v3, v2) in dp.keys():
                        if dp[(v3, v2)]:
                            ok = False
                            dp[(v2, v1)] = False
                    else:
                        inv = True
                        stack.append((v3, v2))
            if inv:
                continue
            else:
                dp[stack.pop()] = ok
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
    ok = False
    for w in g[r]:
        if win(w, r):
            ok = True
            break
    if ok:
        print("Ron")
    else:
        print("Hermione")