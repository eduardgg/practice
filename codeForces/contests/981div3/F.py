
mod = 10**9 + 7
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    x, y = 1, 1
    if k == 1:
        p = 1
    else:
        p = 2
        while y:
            x, y = y, (x+y) % k
            p += 1
    print(n * p % mod)    
