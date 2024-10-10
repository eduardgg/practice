
from math import *
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cur = 0
    for i in range(1, n):
        cur += ceil(log2(a[i-1]/a[i]))
        cur = max(cur, 0)
        ans += cur
    print(ans)