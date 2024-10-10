
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)

    ans = []
    for e in a:
        for k in range(4):
            i = e-e%4+k
            if c.get(i, 0):
                ans.append(i)
                c[i] -= 1
                break
    
    print(*ans)