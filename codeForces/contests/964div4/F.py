
from collections import Counter

mod = 10**9 + 7

def init_fact(n):
    fact = [1]
    for i in range(n):
        fact.append((fact[-1]*(i+1)) % mod)
    invfact = [pow(fact[-1], -1, mod)]
    for i in range(n, 0, -1):
        invfact.append((invfact[-1]*i) % mod)
    invfact = invfact[::-1]
    return fact, invfact

fact, invfact = init_fact(2*(10**5))

def choose(n, k, m):
    if n < 0 or k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] * invfact[n-k]) % m

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    uns = Counter(list(map(int, input().split())))[1]
    ans = 0
    for i in range((k + 1) // 2, min(uns, k) + 1):
        ans += choose(uns, i, mod) * choose(n-uns, k-i, mod)
        ans %= mod
    print(ans)