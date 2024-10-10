
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    s = set()
    ans = 0
    for e in a:
        s.add(e)
        c[e] -= 1
        if not c[e]: ans += len(s)
    print(ans)