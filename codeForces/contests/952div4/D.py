
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    minx, maxx, miny, maxy = m, -1, n, -1
    for i in range(n):
        l = input()
        for x in range(m):
            if l[x] == '#':
                minx = min(minx, x)
                maxx = max(maxx, x)
                miny = min(miny, i)
                maxy = max(maxy, i)
    x = (minx + maxx) // 2 + 1
    y = (miny + maxy) // 2 + 1
    print(y, x)