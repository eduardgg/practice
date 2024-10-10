
from math import log2, ceil
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    last = 0
    for i in range(1, n):
        if a[i-1] == 1:
            continue
        elif a[i] == 1:
            ans = -1
            break
        last += ceil(log2(log2(a[i-1])/log2(a[i])))
        last = max(last, 0)
        ans += last
    print(ans)