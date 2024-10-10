
from math import sqrt
for _ in range(int(input())):
    r = int(input())
    ans = 4
    for x in range(1, r+1):
        # r^2 <= x^2 + y^2 < (r+1)^2
        y1 = int(sqrt(r**2 - x**2))
        y2 = int(sqrt((r+1)**2 - x**2))
        if y1**2 != r**2 - x**2: y1 += 1
        if y1 == 0: y1 += 1
        if y2**2 == (r+1)**2 - x**2: y2 -= 1
        ans += 4*(y2-y1+1)
    print(ans)