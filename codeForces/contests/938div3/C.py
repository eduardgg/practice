
import bisect

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()

    if k >= sum(a):
        print(n)
        continue

    suml, sumr = [0], [0]
    for i in range(n):
        suml.append(suml[-1]+a[i])
        sumr.append(sumr[-1]+a[-1-i])
    
    bl = bisect.bisect_right(suml, (k+1)//2)-1
    br = bisect.bisect_right(sumr, k//2)-1
    print(min(bl+br, n))