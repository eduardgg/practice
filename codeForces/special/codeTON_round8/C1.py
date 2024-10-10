
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, x, y = line()
    a = line()
    a.sort()
    ext = 0
    for i in range(x-1):
        if a[i+1]-a[i] == 2:
            ext += 1
    if a[0] + (n-a[-1]) == 2:
        ext += 1
    ans = ext + x - 2 
    print(ans)