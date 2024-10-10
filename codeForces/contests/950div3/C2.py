
from collections import Counter

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    b = line()
    m = int(input())
    d = line()

    c1 = Counter((b[i] for i in range(n) if a[i] != b[i]))
    c2 = Counter(d)
    print("YES" if c1 <= c2 and d[-1] in b else "NO")