from heapq import heapify, heappop, heappush
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, l = line()
    v = []
    ok = False
    for _ in range(n):
        a, b = line()
        if a <= l:
            ok = True
        v.append((b, a))
    if not ok:
        print(0)
        continue
    ans = 1
    v.sort()
    for i in range(n):
        heap = [v[i][1]]
        size = v[i][1]
        if size > l:
            continue
        num = 1
        for j in range(i+1, n):
            heappush(heap, -v[j][1])
            size += v[j][1] + (v[j][0] - v[j-1][0])
            num += 1
            while size > l and num > ans:
                size += heappop(heap)
                num -= 1
            ans = max(ans, num)
    print(ans)