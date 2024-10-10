
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

def init_stirling(n):
    stirling = [[0 for _ in range(n+1)] for _ in range(n+1)]
    stirling[1][1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            stirling[i][j] = stirling[i-1][j-1] + (i-1)*stirling[i-1][j]
    return stirling

def choose(n, k, m):
    if n < 0 or k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] * invfact[n-k]) % m


def fg(m, k):
    suma = 0
    for c in range(m):
        x = choose(m-1, c, mod)
        y = stirling[c+1][k]
        z = pow(m, m-1-c, mod)
        suma += x*y*z
        suma %= mod
    return suma

n = int(input())
fact, invfact = init_fact(n)
stirling = init_stirling(n)
for k in range(n):
    print(fg(n, k+1))