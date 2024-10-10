
from collections import defaultdict
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    d = defaultdict(list)
    for e in a:
        d[e%k].append(e)
    ans = 0
    senar = False
    for v in d.values():
        v.sort()
        if len(v)%2:
            if n%2 and not senar:
                senar = True
                if len(v) == 1:
                    continue
                dp = [0, v[1]-v[0]]
                for i in range(2, len(v)):
                    dp.append(v[i]-v[i-1]+dp[i-2])
                    if not i%2 and dp[i-1] < dp[-1]:
                        dp[-1] = dp[i-1]
                ans += dp[-1] // k
                continue
            else:
                ans = -1
                break
        for i in range(len(v)//2):
            ans += (v[2*i+1] - v[2*i]) // k
    print(ans)