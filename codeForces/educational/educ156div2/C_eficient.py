t = int(input())
resultat = ""

for _ in range(t):
    s = input()
    pos = int(input())
    l = len(s)
    j = 1
    stack = [0]
    fet = False

    if pos <= l:
        resultat += s[pos-1]
        continue

    while j < len(s):
        
        while stack and pos > l and (s[stack[-1]] > s[j]):
            stack.pop()
            pos -= l
            l -= 1
        
        if not stack or (pos > l and s[stack[-1]] <= s[j]):
            stack.append(j)
            j += 1
        
        if pos <= l:
            if len(stack) >= pos:
                resultat += s[stack[pos-1]]
            else:
                resultat += s[j + pos - len(stack) - 1]
            fet = True
            break

    if fet:
        continue

    else:
        while pos > l:
            stack.pop()
            pos -= l
            l -= 1
        resultat += s[stack[pos-1]]
        continue        
        
print(resultat)