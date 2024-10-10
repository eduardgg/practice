
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    a.sort()
    i = (n+1)//2-1
    ans = 1
    while i<n-1 and a[i+1] == a[i]:
        i += 1
        ans += 1
    print(ans)