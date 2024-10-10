
mod = 998244353
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sums = [a[0]]
    for e in a[1:]:
        sums.append(sums[-1] + e)
    mi = min(sums)
    if mi >= 0:
        print(pow(2, n, mod))
        continue
    ans = 0
    combs = 1
    for i in range(n):
        if sums[i] == mi:
            ans = (ans + combs * pow(2, n-1-i, mod)) % mod
        elif sums[i] >= 0:
            combs = (combs * 2) % mod
    
    print(ans)