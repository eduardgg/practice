
# ACCEPTED

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    V = [(a[i], i) for i in range(n)]
    V.sort()

    resultats = [-1]*k
    posicio = n-1
    maxim = 0
    minim = n-1
    for i in range(k-1, -1, -1):
        if posicio < 0:
            break
        if V[posicio][0] > i+1:
            continue
        while V[posicio][0] == i+1:
            maxim = max(maxim, V[posicio][1])
            minim = min(minim, V[posicio][1])
            resultats[i] = max(resultats[i], maxim - minim)
            posicio -= 1
            if posicio < 0:
                break

    for e in resultats:
        print(2*e+2, end=" ")
    print()