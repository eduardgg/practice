
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    if k == 1:
        v = [i+1 for i in range(n)]
        print(*v)
    elif k == n:
        v = [1 for i in range(n)]
        print(*v)
    else:
        print(-1)