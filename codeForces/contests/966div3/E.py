
for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    w = int(input())
    a = list(map(int, input().split()))
    v = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            v.append(min(i, n+1-i, k, n+1-k)*min(j, m+1-j, k, m+1-k))
    v.sort()
    a.sort()
    ans = 0
    while a:
        ans += v.pop()*a.pop()
    print(ans)