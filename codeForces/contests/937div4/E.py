
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
    while n > 1 and primers[n] != 0:
        f.append(primers[n])
        n //= primers[n]
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


primers = sieve(200000)
for _ in range(int(input())):
    n = int(input())
    s = input()
    d = divisors(n)
    for e in d:
        ok = True
        er = 0
        for i in range(e):
            pri, sec = s[i], None
            npri = 0
            for j in range(n//e):
                if s[i + j*e] == pri:
                    npri += 1
                else:
                    if not sec:
                        er += 1
                        if er > 1:
                            ok = False
                            break
                        sec = s[i + j*e]
                        nsec = 1
                    elif s[i + j*e] != sec:
                        ok = False
                        break
                    else:
                        nsec += 1
                if sec and nsec > 1 and npri > 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            print(e)
            break