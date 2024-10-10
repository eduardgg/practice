
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = Counter(list(map(int, input().split())))
    print("YES" if any([True if a[i]%2 else False for i in a.keys()]) else "NO")