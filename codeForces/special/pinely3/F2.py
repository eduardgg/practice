
# Sembla que funciona bastant bé, però fallen alguns test cases molt puntuals
# No sé a què és degut, les funcions de combinatòria modular semblen ben implementades

def mod_inverse(x, m):
    _, result, _ = extended_gcd(x, m)
    return result % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def comb_mod(n, k, m):
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(min(k, n - k)):
        result = (result * (n - i) % m) * mod_inverse(i+1, m) % m
    return result

def fact_mod(n, m):
    if n < 0:
        return 0
    fact = 1
    for i in range(n):
        fact = (fact * (i+1)) % m
    return fact

def perms_mod(n, k, m):
    if k < 0 or k > n:
        return 0
    perms = 1
    for i in range(k):
        perms = (perms * (n-i)) % m
    return perms



MOD = 998244353
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
    v = list(map(int, input().split()))
    if v[-1] not in {n, -1}:
        print(0)
        continue
    i = 0
    combs = 1
    inicial = i
    for j in range(inicial+1, n):
        if v[j] == -1:
            continue
        if v[i] == -1:
            combs *= perms_mod(j+1, v[j], MOD)
            i = j
            continue
        nous = v[j] - v[i]
        if v[j] > j+1 or nous > 2*(j-i) or nous < 0:
            combs = 0
            break
        suma = 0
        for h in range(0, min(i+1-v[i], nous)+1):
            # print("calculs1: ", comb(i+1-v[i], h), comb(j-i, h), factorial(h), comb(j-h-v[i]+1, nous-h), comb(j-i, nous-h), factorial(nous-h), suma)
            suma += comb_mod(i+1-v[i], h, MOD)*perms_mod(j-i, h, MOD)*comb_mod(j-h-v[i]+1, nous-h, MOD)*perms_mod(j-i, nous-h, MOD)
            suma %= MOD
            # print("info1: ", i, j, nous, h, suma)
            # Potser cal fer les operacions combinatòriques manualment degut als grans nombres i l'eficiència modular
        combs *= suma
        combs %= MOD
        i = j
        if combs == 0:
            break
    
    if combs == 0:
        print(combs)
        continue

    if j == n-1 and i < j:
        if v[i] == -1:
            print(fact_mod(n, MOD))
            continue
        suma = 0
        nous = n - v[i]
        for h in range(0, min(i+1-v[i], nous)+1):
            # print("info2: ", i, j, nous, h, suma)
            suma += comb_mod(i+1-v[i], h, MOD)*perms_mod(j-i, h, MOD)*comb_mod(j-h-v[i]+1, nous-h, MOD)*perms_mod(j-i, nous-h, MOD)
            # print("calculs2: ", comb(i+1-v[i], h), comb(j-i, h), factorial(h), comb(j-h-v[i]+1, nous-h), comb(j-i, nous-h), factorial(nous-h), suma)
            suma %= MOD
        combs *= suma
        combs %= MOD

    print(combs)