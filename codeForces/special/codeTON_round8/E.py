
mod = 998244353
fact = [1]
for i in range(10**6):
    fact.append((fact[-1]*(i+1)) % mod)
invfact = [pow(fact[-1], -1, mod)]
for i in range(10**6, 0, -1):
    invfact.append((invfact[-1]*i) % mod)
invfact = invfact[::-1]

def choose(n, k, m):
    if n < 0 or k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] * invfact[n-k]) % m

for _ in range(int(input())):
    l, n = list(map(int, input().split()))

    comb1 = [1]
    for k in range(1, l-2*n+1):
        comb1.append(choose(2*n+k, k, mod))

    comb2 = [1]
    for k in range(1, l-2*n+1):
        comb2.append(choose(n+k-1, k, mod))
        if k%2: comb2[-1] *= (-1)
    
    conv = 0
    for i in range(l-2*n+1):
        conv += comb1[i]*comb2[l-2*n-i]
        conv %= mod
    
    total = choose(l, 2*n, mod)
    ans = 2*(total - conv) % mod
    print(ans)