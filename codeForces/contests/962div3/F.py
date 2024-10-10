
from heapq import heappush, heappop

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l, r = 0, 10**9
    while r-l > 1:
        m = (r+l)//2
        ops = 0
        for i in range(n):
            ops += max(0, (a[i]-m)//b[i] + 1)
        if ops <= k:
            r = m
        else:
            l = m
    
    ans = 0
    ops = 0
    h = []
    for i in range(n):
        new = max(0, (a[i]-r)//b[i] + 1)
        ops += new
        ans += new*a[i] - b[i]*new*(new-1)//2
        heappush(h, (-(a[i]-b[i]*new), i))

    while ops < k:
        val, i = heappop(h)
        if val >= 0:
            break
        ans += (-val)
        heappush(h, (-(-val-b[i]), i))
        ops += 1
    
    print(ans)