
for _ in range(int(input())):
    n = int(input())
    m = []
    for _ in range(n):
        m.append(list(map(int, input().split())))
    minDiag = [0]*(2*n-1)
    for i in range(n):
        for j in range(n):
            minDiag[n-1+i-j] = min(minDiag[n-1+i-j], m[i][j])
    print(-sum(minDiag))