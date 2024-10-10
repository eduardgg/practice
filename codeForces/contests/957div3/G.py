
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

fact, invfact = init_fact(5000)

def choose(n, k, m):
    if n < 0 or k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] * invfact[n-k]) % m


for _ in range(int(input())):
    n = int(input())
    ans = 0
    for card in range(n+1):
        if 2*card < n:
            for i in range(card, 2*card + 1):
                esq = choose(i, i-card, mod)
                dre = choose(n-i-1, 2*card - i, mod)
                ans = (ans + (i+1) * esq * dre) % mod
        else:
            ans = (ans + (2*card+1) * choose(n, card, mod)) % mod
    print(ans)