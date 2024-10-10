
# He arreglat una mica el temps fent una implementació
# en arrays per dp, en lloc de diccionaris, i alguna
# altra estructura de dades, però segueix fallant.

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    els = set(a)
    used = set()
    dp = [0]*(n+1)
    c = [0]*(n+1)
    for e in a: c[e] += 1
    extra = 0
    ans = n*(n-1)//2

    for e in range(n, 0, -1):
        s = c[e]
        for k in range(2*e, n+1, e):
            dp[e] -= dp[k]
            if e in els and k not in els and k not in used:
                used.add(k)
                extra += dp[k]
            s += c[k] 
        dp[e] += s*(s-1)//2
        if e in els: ans -= dp[e]

    ans -= extra
    print(ans)