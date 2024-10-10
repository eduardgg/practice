t = int(input())
for _ in range(t):
    s = input()
    z, u = 0, 0
    for i in s:
        if i == '0':
            z += 1
        else:
            u += 1
    
    i = 0
    while u >= 0 and z >= 0 and i < len(s):
        if s[i] == '1':
            if z == 0:
                break
            z -= 1
        else:
            if u == 0:
                break
            u -= 1
        i += 1
    print(len(s)-i)