
def factorize(n):
    F = {}
    for p in primers:
        if n in primers:
            F[n] = F.get(n, 0) + 1
            break
        if p*p > n:
            break
        while n % p == 0:
            F[p] = F.get(p, 0) + 1
            n //= p
    if n > 1000:
        # Assumim que és primer, ja que l'entrada és >= 10^6
        F[n] = 1
    return F



t = int(input())

v = [0, 0] + [1]*999
for i in range(2, 1001):
    if v[i] == 0:
        continue
    if v[i] == 1:
        j = 2*i
        while j <= 1000:
            v[j] = 0
            j += i
primers = [p for p in range(1001) if v[p] == 1] 

for _ in range(t):
    n, q = list(map(int, input().split()))
    
    nIni = n
    factN = factorize(n)
    factNini = {i: factN[i] for i in factN.keys()}
    
    for _ in range(q):
        qi = input().split()
        if len(qi) == 1:
            n = nIni
            factN = {i: factNini[i] for i in factNini.keys()}
            continue
        x = int(qi[1])
        factX = factorize(x)

        n *= x
        for k in factX.keys():
            factN[k] = factN.get(k, 0) + factX[k]
    
        div = 1
        for k in factN.keys():
            div *= (factN[k]+1)
        
        if n % div == 0:
            print("YES")
        else:
            print("NO")
        # print("         ", n, div)
        # print("         ", factN)
    print()