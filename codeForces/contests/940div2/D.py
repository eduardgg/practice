
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    le = [[0 for _ in range(30)] for _ in range(n+1)]
    ri = [[0 for _ in range(30)] for _ in range(n+1)]
    for i in range(n):
        for k in range(30):
            if a[i] & (1<<k):
                le[i+1][k] = 1 + i - le[i][k]
            else:
                le[i+1][k] = le[i][k]
            if a[-1-i] & (1<<k):
                ri[-2-i][k] = 1 + i - ri[-1-i][k]
            else:
                ri[-2-i][k] = ri[-1-i][k]

    ans = 0
    for y in range(n):
        k = a[y].bit_length() - 1
        ans += le[1+y][k]*(n-y-ri[y][k]) + (1+y-le[1+y][k])*ri[y][k]
    print(ans)