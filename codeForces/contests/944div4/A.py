
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    x, y = line()
    print(min(x,y), max(x, y))