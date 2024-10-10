from collections import defaultdict

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    ans = 0
    g1, g2, g3, t = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
    for i in range(n-2):
        ans += g1[(a[i], a[i+1])] + g2[(a[i+1], a[i+2])] + g3[(a[i], a[i+2])] - 3*t[(a[i], a[i+1], a[i+2])]
        g1[(a[i], a[i+1])] += 1
        g2[(a[i+1], a[i+2])] += 1
        g3[(a[i], a[i+2])] += 1
        t[(a[i], a[i+1], a[i+2])] += 1
    print(ans)