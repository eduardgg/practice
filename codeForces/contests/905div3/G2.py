
from bisect import bisect_left

line = lambda : list(map(int, input().split()))

def remove(a, b):
    # a and b must be sorted
    rem = 0
    i, j = 0, 0
    while j < len(a):
        if a[i] < b[j]:
            i += 1
            j += 1
        else:
            j += 1
            rem += 1
    return rem

for _ in range(int(input())):
    n, m = line()
    a = line()
    b = line()
    a.sort()
    b.sort()
    # From which m an extra removal will be needed?
    lval = remove([1]+a, b)
    posm = bisect_left(a, m)
    rval = remove(a[:posm]+[m]+(a[posm:] if posm<n else []), b)
    if lval == rval:
        ans = lval*m
    else:
        l, r = 1, m
        # l: Last value for m such that removals = lval
        # r: first value for m such that removals = rval = 1 + lval
        while r-l > 1:
            mid = (r+l)//2
            posmid = bisect_left(a, mid)
            if remove(a[:posmid]+[mid]+(a[posmid:] if posmid<n else []), b) == lval:
                l = mid
            else:
                r = mid
        ans = l*lval + (m-l)*rval
    print(ans)