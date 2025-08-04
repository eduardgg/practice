
n = int(input())
m = list(map(int, input().split())) + [0]
ans = 0
stack = [(-1, -1)]
for i in range(n+1):
    while stack and m[i] <= stack[-1][0]:
        ans = max(ans, stack[-1][0]*(i-stack[-2][1]-1))
        stack.pop()
    stack.append((m[i], i))
print(ans)