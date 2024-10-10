
import bisect
 
n, m = list(map(int, input().split())) 
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
 
v = [(a[i], a[i]-b[i]) for i in range(n)]
v.sort()
a.sort()
 
p = []
cur = float('inf')
for ea, dif in v:
    cur = min(cur, dif)
    p.append(cur)
    
ans = 0
for e in c:
    while e >= a[0]:
        i = bisect.bisect_right(a, e)
        ops = (e - a[i-1]) // p[i-1] + 1
        ans += ops
        e -= ops * p[i-1]
 
ans *= 2
print(ans)