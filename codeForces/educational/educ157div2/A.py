
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    x, y, k = line()
    if x >= y:
        print(x)
    elif x+k >= y:
        print(y)
    else:
        print(2*y-x-k)