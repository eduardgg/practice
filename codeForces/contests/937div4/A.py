
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    a, b, c = line()
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")