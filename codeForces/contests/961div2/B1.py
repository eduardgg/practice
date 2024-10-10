
from collections import Counter
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    d = Counter(a)
    best = 0
    for k in d.keys():
        
        left = m

        q0 = d[k]
        punts = k*min(q0, m//k)
        q0 -= min(q0, m//k)
        left -= punts

        q1 = d.get(k+1, 0)
        new = (k+1)*min(q1, left//(k+1))
        punts += new
        q1 -= min(q1, left//(k+1))

        left -= new
        punts += min(left, d[k]-q0, q1)

        best = max(best, punts)

    print(best)