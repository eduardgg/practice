from collections import defaultdict
from math import lcm

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    a.sort()
    cjt = set(a)
    lcmt = 1
    for e in a: lcmt = lcm(lcmt, e)
    if lcmt != a[-1]:
        print(n)
        continue

    # dp: lcm -> max(len(subsequence))
    dp = defaultdict(int)
    dp[1] = 0
    for e in a:
        for k in list(dp.keys()):
            l = lcm(k, e)
            dp[l] = max(dp[l], dp[k]+1)

    dp[0] = 0
    print(max([dp[k] for k in dp.keys() if k not in cjt]))