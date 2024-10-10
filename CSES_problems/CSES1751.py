
n = int(input())
t = [0] + list(map(int, input().split()))
ans = [0]*(n+1)

vist = [False]*(n+1)
for i in range(1, n+1):
    if not vist[i]:
        vist[i] = True
        stack = [i]
        while not vist[t[i]]:
            vist[t[i]] = True
            stack.append(t[i])
            i = t[i]
        if ans[t[i]]:
            while stack:
                i = stack.pop()
                ans[i] = ans[t[i]] + 1
        else:
            j = stack.index(t[i])
            l = len(stack)-j
            for k in range(l):
                ans[stack.pop()] = l
            while stack:
                i = stack.pop()
                ans[i] = ans[t[i]] + 1

print(*ans[1:])