
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    h, n = line()
    a = line()
    c = line()
    if sum(a) >= h:
        print(1)
        continue
    else:
        top = 0
        for i in range(n):
            top = max(top, a[i]//c[i])
        l, r = 1, 4*(10**10)
        while r - l > 1:
            m = (l + r) // 2
            dam = 0
            for i in range(n):
                dam += a[i] * (1 + (m-1)//c[i])
            if dam >= h:
                r = m
            else:
                l = m
        print(r)