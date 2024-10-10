
from bisect import bisect_left

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, f, k = line()
    a = line()
    fav = a[f-1]
    a.sort()
    i1 = bisect_left(a, fav)
    i2 = bisect_left(a, fav+1)
    if i2 <= n-k: print("NO")
    elif i1 >= n-k: print("YES")
    else: print("MAYBE")