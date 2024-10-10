
line = lambda : list(map(int, input().split()))
mod = 10**9 + 7

dp = [1, 1] + [0]*(300000-1)
for i in range(2, 300000+1):
    dp[i] = dp[i-1] + 2*(i-1)*dp[i-2]
    dp[i] %= mod

for _ in range(int(input())):
    n, k = line()
    for _ in range(k):
        r, c = line()
        n -= 1 + (r != c)
    print(dp[n])