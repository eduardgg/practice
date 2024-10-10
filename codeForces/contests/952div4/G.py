
mod = 10**9 + 7
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    l, r, k = line()
    if k >= 10:
        print(0)
        continue
    combr = pow(10//k + (10%k != 0), r, mod)
    combl = pow(10//k + (10%k != 0), l, mod)
    ans = (combr - combl) % mod
    print(ans)