
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    for e in a:
        suma = e
        x = 1
        while stack and stack[-1][0] >= suma // x:
            suma += stack[-1][0] * stack[-1][1]
            x += stack[-1][1]
            stack.pop()
        stack.append((suma // x, x - (suma % x)))
        if suma % x : stack.append((suma // x + 1, suma % x))
    ans = stack[-1][0] - stack[0][0]
    print(ans)