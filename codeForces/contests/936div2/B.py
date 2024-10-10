
mod = 10**9 + 7
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, k = line()
    a = line()
    cur = 0
    top = 0
    for e in a:
        cur += e
        cur = max(cur, 0)
        top = max(top, cur)
    suma = sum(a) % mod
    for i in range(k):
        suma = (suma + top) % mod
        top = (2 * top) % mod       
    print(suma)