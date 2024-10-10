
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    m, x = line()
    c, h = [], []
    for i in range(m):
        cc, hh = line()
        c.append(cc)
        h.append(hh)
    dp = [[-1 for _ in range(sum(h)+1)] for _ in range(m)]
    dp[0][0] = x
    if c[0] == 0: dp[0][h[0]] = x
    sumh = h[0]
    for d in range(1, m):
        for hh in range(sumh + 1):
            if dp[d-1][hh] != -1:
                dp[d][hh] = max(dp[d][hh], dp[d-1][hh] + x)
            if dp[d-1][hh] != -1 and c[d] <= dp[d-1][hh]:
                dp[d][hh + h[d]] = max(dp[d][hh + h[d]], dp[d-1][hh] + x - c[d])
        sumh += h[d]
    # print(dp)
    toph = 0
    for i in range(len(dp[m-1])):
        if dp[m-1][i] != -1: toph = i
    print(toph)