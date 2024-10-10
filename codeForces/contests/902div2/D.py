
# Funciona, però Time Limit

n = int(input())
a = list(map(int, input().split()))
c = [(a[i], i) for i in range(n)]
c.sort()
c = c[::-1]
bigMod = 998244353

blancs = [False]*n
b = 0
ans = 0
i = 0
while i < n:
    # Assumim c[i] el primer negre/verd. Òbviament és el valor màxim.
    (punts, pos) = c[i]

    if blancs[pos]:
        i += 1
        # No pot anar-hi un verd o negre, ja és blanc.
        # A més també s'hauran pintat de blanc els índexos divisors prèviament.
        continue
    
    # Trobem el número de repeticions de l'element:
    k = 0
    bPrevi = b
    while i+k < n and c[i+k][0] == punts:
        # Marquem blancs per la següent iteració:
        pos = c[i+k][1]
        for j in range(pos+1):
            if (pos+1) % (j+1) == 0 and not blancs[j]:
                blancs[j] = True
                b += 1
        k += 1

    # print(n-bPrevi, n-b, punts, ans, "     ", blancs)
    ans += (2**(n-bPrevi) - 2**(n-b)) * punts
    ans %= bigMod
    i += k
    
print(ans)