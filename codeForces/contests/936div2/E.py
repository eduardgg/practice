
mod = 10**9 + 7
line = lambda : list(map(int, input().split()))

def choose(n, k, m):
    if n < 0 or k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] * invfact[n-k]) % m

fact = [1]
for i in range(2*(10**5)):
    fact.append((fact[-1]*(i+1)) % mod)
invfact = [pow(fact[-1], -1, mod)]
for i in range(2*(10**5), 0, -1):
    invfact.append((invfact[-1]*i) % mod)
invfact = invfact[::-1]

for _ in range(int(input())):
    n, m1, m2 = line()
    p = line()
    s = line()
    if p[0] != 1 or p[-1] != s[0] or s[-1] != n:
        print(0)
    else:
        # Primer escollim quins elements van a l'esquerra:
        # Això és (n-1) sobre (p[-1]-1)
        ans = choose(n-1, p[-1]-1, mod)
        for i in range(1, m1):
            ans = (ans * fact[p[-i]-2] * invfact[p[-i-1]-1]) % mod
        ss = [n+1-e for e in s[::-1]]
        for i in range(1, m2):
            ans = (ans * fact[ss[-i]-2] * invfact[ss[-i-1]-1]) % mod
        print(ans)