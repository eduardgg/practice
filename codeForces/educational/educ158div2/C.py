t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m, M = min(a), max(a)
    ops = 0
    while m != M:
        M = (M + m) // 2
        ops += 1
    print(ops)
    if 0 < ops <= n:
        for i in range(ops):
            print(m, end=" ")
        print()
