
line = lambda : list(map(int, input().split()))
for t in range(int(input())):
    n, k = line()
    a = []
    c = []
    i = 0
    while n > 0:
        k = min(n, k)
        i += 1
        c += [i]*k
        ind = [i for i in range(k//2, k)] + [i for i in range(k//2)]
        a += [len(a)+1+j for j in ind]
        n -= k

    print(*a)
    print(c[-1])
    print(*c)