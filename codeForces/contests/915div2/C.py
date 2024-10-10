
for _ in range(int(input())):
    n = int(input())
    s = input()

    v = [(s[i], -i) for i in range(n)]
    v.sort()
    trans = []
    pos = -1
    for (e, i) in v[::-1]:
        if -i > pos:
            trans.append(e)
            pos = -i
    
    new = []
    j = 0
    for i in range(n):
        if trans[j] == trans[0]:
            aux = j
        if j < len(trans) and s[i] == trans[j]:
            new.append(trans[-1-j])
            j += 1
        else:
            new.append(s[i])

    ok = True
    for i in range(1, n):
        if new[i] < new[i-1]:
            ok = False
            break

    print(len(trans)-1-aux if ok else -1)