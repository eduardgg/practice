
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()
    x = line()
    v = []
    for i in range(n):
        v.append((abs(x[i]), a[i]))
    v.sort()
    
    suma = 0
    ok = True
    for i in range(n):
        suma += v[i][1]
        if suma - k*v[i][0] > 0:
            ok = False
            break
    
    if ok:
        print("YES")
    else:
        print("NO")