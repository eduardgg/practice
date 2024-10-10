
# Codi més senzill, però usa pop(i), i per tant té cost O(n^2)

t = int(input())
for _ in range(t):
    n = int(input())
    e = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        e += [(a, i)]
        e += [(b, i)]
    e.sort()

    dins = []
    resultat = 0
    while e:
        (c, i) = e.pop()
        if i not in dins:
            dins += [i]
        else:
            j = len(dins)-1
            while dins[j] != i:
                j -= 1
            resultat += j
            dins.pop(j)
    print(resultat)