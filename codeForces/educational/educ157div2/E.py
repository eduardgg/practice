
import bisect

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):

    n = int(input())
    ax = line()
    ay = line()
    a = [(ax[i], ay[i]) for i in range(n)]
    a.sort()
    ma = 0
    maxa = []
    for i in range(n):
        if ma < a[-1-i][1]:
            j = n-1-i
            ma = a[-1-i][1]
        maxa.append(j)
    maxa = maxa[::-1]

    m = int(input())
    bx = line()
    by = line()
    b = [(bx[i], by[i]) for i in range(m)]    
    b.sort()
    mb = 0
    maxb = []
    for i in range(m):
        if mb < b[-1-i][1]:
            j = m-1-i
            mb = b[-1-i][1]
        maxb.append(j)
    maxb = maxb[::-1]

    guanya = [False]*n
    perd = [False]*n
    vist = [False]*n
    for i in range(n):
        if vist[i]:
            continue
        vist[i] = True
        stack = [i]
        while stack:
            j = bisect.bisect_left(b, (a[stack[-1]][1], 10**6+1))
            if j >= m:
                # b no pot tirar => guanya a
                while stack:
                    guanya[stack.pop()] = True
            else:
                k = bisect.bisect_left(a, (b[maxb[j]][1], 10**6+1))
                if k >= n:
                    # a no pot tirar => guanya b
                    while stack:
                        perd[stack.pop()] = True
                    continue
                k = maxa[k]
                if vist[k] and guanya[k]:
                    while stack:
                        guanya[stack.pop()] = True
                elif vist[k] and perd[k]:
                    while stack:
                        perd[stack.pop()] = True
                elif vist[k]:
                    break
                else:
                    vist[k] = True
                    stack.append(k)

    w, d, l = 0, 0, 0
    for i in range(n):
        if guanya[i]:
            w += 1
        elif perd[i]:
            l += 1
        else:
            d += 1
    print(w, d, l)