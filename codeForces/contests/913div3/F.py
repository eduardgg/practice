
# El truc està en veure que l'ordre relatiu dels elements
# és sempre el mateix (en cicle), sigui el que sigui el 
# nombre de shifts o reverses que fem.
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    inc, dec = 0, 0
    for i in range(n):
        if a[i] > a[i-1]:
            j = i
            inc += 1
        if a[i] < a[i-1]:
            k = i
            dec += 1
    
    # O les dues (inc i dec) són 0, o cap d'elles
    # Si són zero, tots els elements són iguals.
    if dec == 0:
        print(0)
        continue
    
    # Cas impossible d'arreglar:
    if inc > 1 and dec > 1:
        print(-1)
        continue

    op1, op2 = n+2, n+2

    if inc == 1:
        if j == 0:
            # Està ordenat al revés, només cal fer reverse:
            print(1)
            continue
        else:
            op1 = min(j+1, n-j+1)

    if dec == 1:
        if k == 0:
            # Ja està ordenat
            print(0)
            continue
        else:
            op2 = min(k+2, n-k)
    
    ans = min(op1, op2)
    print(ans)
