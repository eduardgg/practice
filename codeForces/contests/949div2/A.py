
for _ in range(int(input())):
    l, r = list(map(int, input().split()))
    x = 1
    sc = -2
    while x <= 2*r:
        x *= 2
        sc += 1
    print(sc)