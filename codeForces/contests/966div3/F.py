
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    maxn = 10**9
    dp = [0] + [maxn]*(k+1)
    for i in range(1, n+1):
        a, b = list(map(int, input().split()))
        for p in range(k-1, -1, -1):
            if dp[p] == maxn: continue
            punts = 0
            cost = 0
            ai, bi = a, b
            while ai*bi > 1 and p + punts <= k:
                if ai >= bi: punts += 1; cost += bi; ai -= 1
                else: punts += 1; cost += ai; bi -= 1
                dp[p + punts] = min(dp[p + punts], dp[p] + cost)
            if p + punts + 2 <= k+1:
                dp[p + punts + 1] = min(dp[p + punts + 1], dp[p] + cost + 1)
                dp[p + punts + 2] = min(dp[p + punts + 2], dp[p] + cost + 1)
    ans = dp[k]
    print(-1 if ans == 10**9 else ans)