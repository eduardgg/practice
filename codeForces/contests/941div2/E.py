
for _ in range(int(input())):
    n = int(input())
    s = input()
    pos = 0
    maxim, minim = 0, 0
    dir = True
    for i in range(n-1):
        if s[i+1] == s[i]:
            dir = not dir
        elif dir:
            pos += 1
            maxim = max(maxim, pos)
        else:
            pos -= 1
            minim = min(minim, pos)
    print(maxim - minim + 1)