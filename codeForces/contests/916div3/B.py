
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, k = line()
    v = [i+1 for i in range(n)]
    ans = v[k+1:][::-1] + v[:k+1]
    print(*ans)