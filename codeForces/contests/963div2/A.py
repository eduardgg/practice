
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    c = Counter(input())
    ans = sum([min(n, c[char]) for char in c.keys() if char in {'A', 'B', 'C', 'D'}])
    print(ans)