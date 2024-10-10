t = int(input())
for _ in range(t):
    n = int(input())
    maxx, minx, maxy, miny = 0, 0, 0, 0
    for i in range(n):
        xi, yi = list(map(int, input().split()))
        if xi > maxx:
            maxx = xi
        if xi < minx:
            minx = xi
        if yi > maxy:
            maxy = yi
        if yi < miny:
            miny = yi
    if miny*maxy < 0 and minx*maxx < 0:
        print("NO")
    else:
        print("YES")