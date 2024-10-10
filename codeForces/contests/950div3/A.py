
from collections import defaultdict

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    s = input()
    d = defaultdict(int)
    for c in s: d[c] += 1
    ans = 0
    for k in 'ABCDEFG':
        ans += max(0, m-d[k])
    print(ans)