
import bisect

def f(e):
    if e >= a[-1]:
        ops = (e - a[-1]) // p[-1] + 1
        return ops + f(e - ops * p[-1])
    if e < a[0]:
        return 0
    if dp[e] != -1:
        return dp[e]
    i = bisect.bisect_right(a, e)
    ops = (e - a[i-1]) // p[i-1] + 1
    dp[e] = ops + f(e - ops * p[i-1])
    return dp[e]



n, m = list(map(int, input().split())) 
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

v = [(a[i], a[i]-b[i]) for i in range(n)]
v.sort()
a.sort()

p = []
cur = 10**6
for ea, dif in v:
    cur = min(cur, dif)
    p.append(cur)

ans = 0
dp = [-1] * (10**6 + 1)
for e in c:
    ans += f(e)

ans *= 2
print(ans)