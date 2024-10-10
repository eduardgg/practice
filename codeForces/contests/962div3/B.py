
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    m = []
    for i in range(n):
        m.append(input())
    for i in range(n//k):
        for j in range(n//k):
            print(m[i*k][j*k], end = "")
        print()