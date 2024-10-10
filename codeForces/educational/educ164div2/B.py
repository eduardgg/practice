
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    ok = False
    esq, dre = None, None
    
    millor = n
    cont = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            cont += 1
        elif a[i] != a[0]:
            millor = min(millor, cont)
            cont = 1
        else:
            cont = 1
    millor = min(millor, cont)
    
    if millor == n:
        print(-1)
    else:
        print(millor)