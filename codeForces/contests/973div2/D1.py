
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    stack = [(0, 1), (a[0], 1)]
    for e in a[1:]:
        if e >= stack[-1][0]:
            stack.append((e, 1))
        else:
            while e + (stack[-1][0] - stack[-2][0]) * stack[-1][1] <= stack[-2][0]:
                e += (stack[-1][0] - stack[-2][0]) * stack[-1][1]
                stack[-2] = (stack[-2][0], stack[-2][1] + stack[-1][1])
                stack.pop()
            h, q = stack.pop()
            p = (h - e) // (1 + q)
            e += p*q
            h -= p
            if (h-1)*(h-e): stack.append((h - 1, h - e))
            if h*(q-h+e+1): stack.append((h, q - (h - e) + 1))
    ans = stack[-1][0] - stack[1][0]
    print(ans)