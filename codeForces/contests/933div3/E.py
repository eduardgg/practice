
# Time Limit Exceeded (cost O(n*m*d) massa elevat)
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m, k, d = line()
    res = []
    for i in range(n):
        v = line()
        cost = [1]
        for j in range(1, m):
            minim = min(cost[max(j-1-d, 0):j])
            cost.append(minim + v[j] + 1)
        res.append(cost[-1])
    millor = sum(res[:k])
    cur = millor
    for i in range(n-k):
        cur += res[k+i]-res[i]
        millor = min(millor, cur)
    print(millor)