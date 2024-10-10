
def gcd(n, m):
    if n < m:
        return gcd(m, n)
    if m == 0:
        return n
    return gcd(n%m, m)

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    talls = 0
    mult = gcd(n, m)
    n //= mult
    m //= mult    
    while m%2 == 0:
        n = n%m
        talls += n*mult
        mult *= 2
        m //= 2
    if m != 1:
        print(-1)
    else:
        print(talls)