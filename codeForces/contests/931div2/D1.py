
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, m = line()
    b = n.bit_length() - 1
    p1 = False
    p2 = False
    ok0 = False
    ok1 = False

    while b >= 0:
        if n & m & (1 << b):
            ok1 = True
            break
        if n & (1 << b):
            if p1:
                p2 = True
            else:
                p1 = True
                i = b
        elif m & (1 << b):
            if not p2:
                ok0 = True
            break
        b -= 1

    if ok0:
        print(-1)
    elif ok1:
        print(1)
        print(n, m)
    else:
        print(2)
        print(n, m^n - (1 << i), m)