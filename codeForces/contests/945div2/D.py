
for _ in range(int(input())):

    n, k = list(map(int, input().split()))
    maxim = 1
    while maxim <= n:
        print("?", 1, maxim*n)
        p = int(input())
        if p == n: break
        maxim += 1
    m = maxim
    while m <= maxim*n//k:
        pos = 1
        ints = 1
        ok = False
        while pos <= n and ints <= k:
            print("?", pos, m)
            q = int(input())
            if q == n+1:
                break
            if q == n and ints == k:
                ok = True
                break
            ints += 1
            pos = q+1
        if ok:
            break
        m += maxim
    
    print("!", m if ok else -1)
    res = int(input())