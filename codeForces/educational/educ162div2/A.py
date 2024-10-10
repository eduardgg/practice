
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    primer = False
    zeros = 0
    count = 0
    for i in range(n):
        if a[i] == 1:
            primer = True
            count += zeros
            zeros = 0
        elif primer:
            zeros += 1
    print(count)