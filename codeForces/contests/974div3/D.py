
from collections import Counter
for _ in range(int(input())):
    n, d, k = list(map(int, input().split()))
    e, s = [], []
    for _ in range(k):
        l, r = list(map(int, input().split()))
        e.append(l)
        s.append(r)
    entra, surt = Counter(e), Counter(s)
    current = sum([entra[i] for i in range(1, d+1)])
    mina, mini = current, 1
    maxa, maxi = current, 1
    for i in range(d+1, n+1):
        current += entra[i]
        current -= surt[i-d]
        if current > maxa:
            maxa = current
            maxi = i-d+1
        if current < mina:
            mina = current
            mini = i-d+1
    print(maxi, mini)