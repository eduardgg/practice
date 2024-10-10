from collections import defaultdict

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    ans = 0
    g1, g2, g3 = defaultdict(dict), defaultdict(dict), defaultdict(dict)
    t1, t2, t3 = {}, {}, {}

    for i in range(n-2):

        ans += t1.get((a[i], a[i+1]), 0) - g1[(a[i], a[i+1])].get(a[i+2], 0)
        ans += t2.get((a[i+1], a[i+2]), 0) - g2[(a[i+1], a[i+2])].get(a[i], 0)
        ans += t3.get((a[i], a[i+2]), 0) - g3[(a[i], a[i+2])].get(a[i+1], 0)

        g1[(a[i], a[i+1])][a[i+2]] = g1[(a[i], a[i+1])].get(a[i+2], 0) + 1
        g2[(a[i+1], a[i+2])][a[i]] = g2[(a[i+1], a[i+2])].get(a[i], 0) + 1
        g3[(a[i], a[i+2])][a[i+1]] = g3[(a[i], a[i+2])].get(a[i+1], 0) + 1

        t1[(a[i], a[i+1])] = t1.get((a[i], a[i+1]), 0) + 1
        t2[(a[i+1], a[i+2])] = t2.get((a[i+1], a[i+2]), 0) + 1
        t3[(a[i], a[i+2])] = t3.get((a[i], a[i+2]), 0) + 1
    
    print(ans)