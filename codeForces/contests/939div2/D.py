
def mex(l, r):
    ops.append((l+1, r+1))
    s = set(a[l:r+1])
    for i in range(20):
        if i not in s:
            ans = i
            break
    for i in range(l, r+1):
        a[i] = ans

def make(pos, e):
    if e == 0:
        if a[pos] != 0:
            mex(pos, pos)
            a[pos] = 0
        return
    for i in range(e):
        make(pos+i, e-1-i)
    mex(pos, pos+e-1)

n = int(input())
a = list(map(int, input().split()))
millor, millorc, millorv = 0, 0, []

for i in range(2**n):
    v = []
    count = 0
    res = 0
    for j in range(n):
        if i & (1<<j):
            count += 1
        else:
            res += a[j]
            if count:
                res += count**2
                v.append((j-count, count))
                count = 0
    if count:
        v.append((n-count, count))
        res += (count**2)
    if res > millorc:
        millor, millorc, millorv = i, res, [e for e in v]

ops = []
for (pos, e) in millorv:
    make(pos, e)

print(millorc, len(ops))
for (l, r) in ops:
    print(l, r)
# print(a)