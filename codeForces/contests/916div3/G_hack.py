import random

mod = 998244353
line = lambda : list(map(int, input().split()))


# Test Case: O(n^2) -> Should exceed time limit.
n = 20000
a = list(range(n, 0, -1)) + list(range(1, n+1))


s = set()
ans1, ans2 = 0, 1
    
xors = [random.randint(0, 2**64) for _ in range(n+1)]
# He provat 2**32 però ha fallat. Pot ser per col·lisió?

l, r = 0, 0
while l < 2*n:
    ans1 += 1
    s = {a[l]}
    acxor = xors[a[l]]
    d = {acxor:l}
    no = set()
    while s:
        r += 1
        acxor ^= xors[a[r]]
        if not acxor:
            # minimal closed interval found: (l, r)
            ans2 *= (r-l+1-2*len(no))
            ans2 %= mod
            l, r = r+1, r+1
            break
        elif acxor in d.keys():
            # inner interval found: (d[acxor], r)
            for e in range(d[acxor]+1, r+1):
                no.add(a[e])
        else:
            d[acxor] = r
            
print(ans1, ans2)