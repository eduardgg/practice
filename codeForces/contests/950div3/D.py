
from math import gcd

def dec(j):
    d = a[:j] + a[j+1:]
    c = [gcd(d[i],d[i+1]) for i in range(n-2)]
    for i in range(n-3):
        if c[i] > c[i+1]:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = [gcd(a[i], a[i+1]) for i in range(n-1)]

    ok = True
    for i in range(n-2):
        if b[i] > b[i+1]:
            print('YES' if dec(i) or dec(i+1) or dec(i+2) else "NO")
            ok = False
            break
    if ok: print('YES')