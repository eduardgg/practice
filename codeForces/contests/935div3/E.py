
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, x = line()
    p = line()
    for i in range(n):
        if p[i] == x:
            posx = i+1
            break
    
    print(2)
    print(posx, n)
    p[posx-1], p[n-1] = p[n-1], p[posx-1]
    
    l, r = 1, n+1
    while r-l > 1:
        m = (l+r)//2
        if p[m-1] <= x:
            l = m
        else:
            r = m
    
    p[n-1], p[l-1] = p[l-1], p[n-1]
    print(n, l)