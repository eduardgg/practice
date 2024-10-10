
# Les respostes són correctes, però...
# TIME LIMIT EXCEEDED !!!

t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    k = int(input())

    utils = [(c[i], i) for i in range(n)]

    # Primer, netegem el vector de costos innecessaris.
    # Com més a l'esquerra, menys útil, i per tant ha de ser més barat.
    minim = float('inf')
    for i in range(n):
        if utils[n-1-i][0] >= minim:
            utils.pop(n-1-i)
            continue
        minim = utils[n-1-i][0]

    # El màxim i el mínim no poden diferir en més del doble
    # (si no, sortiria més a compte comprar 2 del cost baix)
    for i in range(1, len(utils)):
        if utils[i][0] >= 2*utils[0][0]:
            utils = utils[:i]
            break
    
    array = [0]*len(c)
    quants = [0]*len(c)
    while utils[0][0] <= k:
        millor = 0
        cost = utils[0][0]
        for (u, i) in utils:
            if k//u == k//utils[0][0]:
                millor = i
                cost = u
            else:
                break
        k -= cost
        
        """
        # La versió fàcil és aquesta:
        for j in range(millor+1):
            array[j] += 1
        # però ho farem més eficient
        """
        quants[millor] += 1
    
    array[-1] = quants[-1]
    for i in range(len(c)-1):
        array[-2-i] = array[-1-i] + quants[-2-i]
    for e in array:
        print(e, end=" ")
    print()