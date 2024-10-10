
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    if bin(n).count('1') % 2 == 0:
        print("first", flush = True)
    else:
        print("second", flush = True)
        p1, p2 = line()
        if p1 < 1:
            continue
        else:
            if bin(p1).count('1') % 2 == 0:
                n = p1
            else:
                n = p2
    while True:
        i = n.bit_length()
        k = 1 << (i-1)
        print(k, n-k, flush = True)
        p1, p2 = line()
        if p1 < 1:
            break
        else:
            if bin(p1).count('1') % 2 == 0:
                n = p1
            else:
                n = p2