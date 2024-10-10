
def median(v):
    l, r = -1, 10**9
    while r-l > 1:
        m = (l + r) // 2
        count = 0
        for e in v:
            if e > m:
                count += 1
        if count <= len(v)//2:
            r = m
        else:
            l = m
    return r


t = int(input())
for tc in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(a[i], b[i]) for i in range(n)]
    c.sort()
    a = [c[i][0] for i in range(n)]
    b = [c[i][1] for i in range(n)]
    top = 0

    # Opció 1: Incrementem el màxim
    i = n - 1
    while i >= 0:
        if a[i] + k > a[-1] and b[i]:
            top = a[i] + k + median(a[:i] + a[i+1:])
            break
        i -= 1

    # Opció 2: Incrementem la mediana
    l, r = 0, a[-1]+1
    while r-l > 1:
        m = (l + r) // 2
        count = 0
        copyk = k
        for i in range(n-2, -1, -1):
            if a[i] >= m:
                count += 1
            elif b[i] and copyk >= m - a[i]:
                count += 1
                copyk -= (m - a[i])
        if count > (len(a) - 1)//2:
            l = m
        else:
            r = m
    
    top = max(top, l + a[-1])
    print(top)