
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n in {1, 2}: print(-1); continue
    a.sort()
    ans = max(0, 2*n*a[n//2] - sum(a) + 1)
    print(ans)