
n, m = list(map(int, input().split()))
r = list(map(int, input().split()))
dp = [0 for _ in range(m+1)]
i = 0
for e in r:
    if e == 0:
        i += 1
    elif e > 0:
        for j in range(e, i+1):
            dp[j] += 1
    else:
        for j in range(-e, i+1):
            dp[i-j] += 1
print(max(dp))