
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    b = line()
    ab = [((a[i]+b[i]), i) for i in range(n)]
    ab.sort()
    while ab:
        (e, i) = ab.pop()
        a[i] -= 1
        b[i] = 0
        if ab:
            (e, i) = ab.pop()
            a[i] = 0
            b[i] -= 1
    print(sum(a)-sum(b))