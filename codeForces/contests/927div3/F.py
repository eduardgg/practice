line = lambda : list(map(int,input().split()))
for _ in range(int(input())):
    n, m = line()
    q = [0]*(n+2)
    acu = [0]*(n+1)
    mins = [i for i in range(n+1)]
    for _ in range(m):
        l, r = line()
        acu[l-1] += 1
        acu[r] -= 1
        mins[r] = min(mins[r], l)
    for i in range(1, n+2):
        q[i] = q[i-1] + acu[i-1]
    for i in range(n):
        mins[n-1-i] = min(mins[n-1-i], mins[n-i])
    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[i-1], q[i] + dp[mins[i]-1])
    print(dp[n])