
from math import gcd
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]
    for e in a[1:]: g = gcd(g, e)
    i = a.index(min(a))
    used = [False]*n
    used[i] = True
    curg = min(a)
    ans = curg
    while curg > g:
        ming = curg
        for i in range(n):
            if not used[i] and gcd(curg, a[i]) <= ming:
                ming = gcd(curg, a[i])
                topg = i
        ans += ming
        curg = ming
        used[topg] = True
    ans += g * (n - sum(used))
    print(ans)