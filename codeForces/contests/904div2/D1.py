
from collections import defaultdict, Counter

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    c = Counter(a)
    els = list(c.keys())
    els.sort(reverse=True)
    dp = defaultdict(int)
    used = {}
    extra = 0

    for e in range(n, 0, -1):
        s = c[e]
        k = 2
        while k*e <= n:
            dp[e] -= dp[k*e]
            if e in els and k*e not in els and not used.get(k*e, False):
                used[k*e] = True
                extra += dp[k*e]
            s += c[k*e] 
            k += 1
        dp[e] += s*(s-1)//2
    
    ans = n*(n-1)//2
    for k in dp.keys():
        if k in els: ans -= dp[k]
    ans -= extra
    print(ans)