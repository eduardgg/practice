
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    a = line()
    a.sort()
    ans = (a[n-1]-a[0])+(a[-1]-a[n])
    print(ans)
    for i in range(n):
        print(a[i], a[i+n])