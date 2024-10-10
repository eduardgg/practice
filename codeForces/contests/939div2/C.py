
for _ in range(int(input())):
    n = int(input())
    p = [i+1 for i in range(n)]
    m = [[0 for _ in range(n)] for _ in range(n)]
    ans = []

    for i in range(n):
        for j in range(n):
            m[-1-i][j] = p[j]
            m[j][-1-i] = p[j]
        ans.append((1, n-i, *p))
        ans.append((2, n-i, *p))

    suma = sum([sum(m[i]) for i in range(n)])
    print(suma, 2*n)
    for v in ans:
        print(*v)