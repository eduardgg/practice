
from math import gcd

def sieve(n):
    sieve = [0]*(n+1)
    x = 2
    while x <= n:
        if sieve[x]:
            x += 1
            continue
        u = 2*x
        while u <= n:
            sieve[u] = x
            u += x
        x += 1
    return sieve

def facto(n):
    f = []
    while n > 1 and s[n] != 0:
        f.append(s[n])
        n //= s[n]
    f.append(n)
    return f

def dicFact(f):
    d = {}
    for i in f:
        d[i] = d.get(i, 0) + 1
    return d

def divisors(n):
    def f(i, d):
        if i == len(v):
            divisors.append(d)
            return
        for j in range(F[v[i]]+1):
            f(i+1, d*(v[i]**j))
    F = dicFact(facto(n))
    divisors = []
    v = []
    for k in F.keys():
        v.append(k)
    f(0, 1)
    divisors.sort()
    return divisors



line = lambda : list(map(int, input().split()))

s = sieve(1000000)

for _ in range(int(input())):

    n, m = line()
    a = []
    for _ in range(n):
        a.append(line())
    
    e = gcd(a[0][0], a[-1][-1])
    div = divisors(e)[::-1]

    for d in div:
        stack = [(0, 0)]
        vist = [[False for _ in range(m)] for _ in range(n)]
        vist[0][0] = True
        ok = False
        while stack:
            (i, j) = stack.pop()
            if i+j == n+m-2:
                ok = True
                break
            if (j+1 < m and not a[i][j+1] % d and not vist[i][j+1]):
                vist[i][j+1] = True
                stack.append((i, j+1))
            if (i+1 < n and not a[i+1][j] % d and not vist[i+1][j]):
                vist[i+1][j] = True
                stack.append((i+1, j))
        if ok:
            print(d)
            break