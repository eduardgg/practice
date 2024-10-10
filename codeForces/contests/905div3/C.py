
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()
    mm = 0
    ok = False
    for e in a:
        if e%k == 0:
            ok = True
            break
        mm = max(mm, e%k)
    if ok:
        print(0)
        continue
    elif k == 4:
        prod = 1
        for e in a: prod *= e
        if prod%2: print(min(2,k-mm))
        elif prod%4: print(1)
        else: print(0)
    else:
        print(k-mm)
