
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, k, pb, ps = line()
    p = line()
    a = line()

    topb = k*a[pb-1]
    i = p[pb-1]
    c = 1
    suma = a[pb-1]
    while i != pb and c < k:
        topb = max(topb, suma + (k-c)*a[i-1])
        suma += a[i-1]
        c += 1
        i = p[i-1]
    
    tops = k*a[ps-1]
    i = p[ps-1]
    c = 1
    suma = a[ps-1]
    while i != ps and c < k:
        tops = max(tops, suma + (k-c)*a[i-1])
        suma += a[i-1]
        c += 1
        i = p[i-1]
    
    if topb > tops:
        print("Bodya")
    elif topb < tops:
        print("Sasha")
    else:
        print("Draw")