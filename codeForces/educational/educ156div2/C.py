t = int(input())
resultat = ""
for _ in range(t):
    s = input()
    pos = int(input())
    l = len(s)
    trobat = False
    while not trobat:
        if pos <= l:
            resultat += s[pos-1]
            trobat = True
            break
        fet = False
        for i in range(l-1):
            if s[i] > s[i+1]:
                s = s[:i] + s[i+1:]
                fet = True
                break
        if not fet:
            s = s[:-1]
        pos -= l
        l -= 1
print(resultat)
