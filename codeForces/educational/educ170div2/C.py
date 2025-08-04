
from collections import deque

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()

    d = deque()
    suma = 0
    for e in a:
        if d and e > d[-1] + 1:
            d.clear()
            d.append(e)
            suma = max(suma, len(d))
            continue
        while d and d[0] <= e-k:
            d.popleft()
        d.append(e)
        suma = max(suma, len(d))
    
    print(suma)