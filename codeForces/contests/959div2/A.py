
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    if n == m == 1: print(-1)
    elif n == 1:
        b = [[a[0][(i+1)%m] for i in range(m)]]
        for v in b: print(*v)
    else:
        b = [a[(i+1)%n] for i in range(n)]
        for v in b: print(*v)