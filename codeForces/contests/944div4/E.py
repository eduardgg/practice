
from bisect import bisect_left as bl

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k, q = line()
    a = [0] + line()
    b = [0] + line()
    
    ans = []
    for _ in range(q):
        d = int(input())
        i = bl(a, d)
        if a[i] == d:
            ans.append(b[i])
        else:
            # Regla de 3 entre (i-1, i):
            x = b[i-1] + (d-a[i-1])*(b[i]-b[i-1])//(a[i]-a[i-1])
            ans.append(x)
    print(*ans)