
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    p = line()
    
    j = p.index(0)
    stack = [j]
    best = cur = n
    for i in range(j + 1, j + n):
        i %= n
        while p[i] < p[stack[-1]]:
            j = stack.pop()
            cur -= p[j] * ((j - stack[-1]) % n)
        j = stack[-1]
        cur += p[i] * ((i - j) % n)
        best = max(best, cur)
        stack.append(i)
    
    print(best)