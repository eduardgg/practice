
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    if k >= n-1:
        print(1)
    else:
        print(n)