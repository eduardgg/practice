
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    long = len(a)
    suma = 0
    sumaPar = 0
    maxBen1 = 0
    maxBen2 = 0
    for i in range(long):
        if a[long-1-i] > 0:
            if (long-1-i) % 2 == 0:
                suma += a.pop(long-1-i)
                suma += sumaPar
                sumaPar = 0
                maxBen1 = 0
                maxBen2 = 0
            else:
                maxBen2 = max(maxBen2, sumaPar)
                sumaPar += a[long-1-i]
        else:
            if (long-1-i) % 2 == 0:
                maxBen1 = max(maxBen1, a[long-1-i] + sumaPar)
            else:
                maxBen2 = max(maxBen2, sumaPar)
    resultat = suma + max(maxBen1, maxBen2)
    print(resultat)