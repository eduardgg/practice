
import bisect

n, m = list(map(int, input().split())) 
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

v = [(a[i], a[i]-b[i]) for i in range(n)]
v.sort()

p = []
a = []
cur = 10**6
for ea, dif in v:
    if dif < cur:
        cur = dif
        p.append(cur)
        a.append(ea)

ans = 0
dp = [-1] * (10**6 + 1)
for e in c:
    if e < a[0]:
        continue
    if e >= a[-1]:
        ops = (e - a[-1]) // p[-1] + 1
        ans += ops
        e -= ops * p[-1]
    
    copy = e
    nums = []
    incrs = []
    while dp[e] == -1:
        if e < a[0]:
            dp[e] = 0
            break
        i = bisect.bisect_right(a, e)
        ops = (e - a[i-1]) // p[i-1] + 1
        nums.append(e)
        incrs.append(ops)
        e -= ops * p[i-1]
    
    while nums:
        new = nums.pop()
        dp[new] = dp[e] + incrs.pop()
        e = new

    ans += dp[copy]

ans *= 2
print(ans)