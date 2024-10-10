t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    if k == 1:
        print(1)
    elif k == 2:
        print(min(m, n-1) + m//n)
    elif k == 3:
        print(m - m//n - min(m, n-1))
    else:
        print(0)