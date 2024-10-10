
# Fórmula: C(n, k) = n!/((n-k)!·k)

n = 10**6
mod = 10**9 + 7
fact = [1]
for i in range(n):
    fact.append((fact[-1]*(i+1)) % mod)
invfact = [pow(fact[-1], -1, mod)]
for i in range(n, 0, -1):
    invfact.append((invfact[-1]*i) % mod)
invfact = invfact[::-1]

sieve = [0]*(n+1)
for x in range(2, n+1):
    if sieve[x]:
        continue
    for u in range(2*x, n+1, x):
        sieve[u] = x

primers = [i for i in range(5, n+1) if not sieve[i]]
# nums = [2,3,4] + primers

c = [0,0,1,3,4]
ac = [0,0,1,4,8]
for i in range(5, 100):
    suma = 0
    for j in [1,2,3,4] + primers:
        if j > i:
            break
        suma += (fact[i]*invfact[i-j]*pow(j,-1,mod)) % j
    print(i, suma)
    c.append(suma % mod)
    ac.append((ac[-1] + c[-1]) % mod)

print(ac[:20])
for _ in range(int(input())):
    n = int(input())
    print(ac[n])