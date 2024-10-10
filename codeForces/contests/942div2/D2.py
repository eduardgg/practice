
from math import gcd, sqrt

for i in range(int(input())):
    n, m = map(int,input().split())
    ans = 0
    for ka in range(1, int(sqrt(n))+1):
        for kb in range(1, int(sqrt(m))+1):
            if gcd(ka, kb) == 1:
                ans += min(n//(ka*(ka+kb)), m//(kb*(ka+kb)))
    print(ans)