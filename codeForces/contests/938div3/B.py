
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, c, d = line()
    b = line()
    b.sort()
    bb = [b[0]+c*i+d*j for i in range(n) for j in range(n)]
    bb.sort()
    if b == bb:
        print("YES")
    else:
        print("NO")