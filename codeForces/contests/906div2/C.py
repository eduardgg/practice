t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    # Primer filtre:
    if n % 2 == 1:
        print(-1)
        continue
    
    # Segon filtre:
    zeros = 0
    uns = 0
    for i in s:
        if i == '0':
            zeros += 1
        else:
            uns += 1
    if zeros != uns:
        print(-1)
        continue

    adds = []
    ok = True

    x = 0
    y = n-1
    while x < y:
        if s[x] != s[y]:
            x += 1
            y -= 1
        elif s[x] == '0':
            # 0...0 -> Afegim 01 al final
            adds.append(y+1)
            s = s[:y+1] + '01' + s[y+1:]
            x += 1
            y += 1
        else:
            # 1...1 -> Afegim 01 a l'inici
            adds.append(x)
            s = s[:x] + '01' + s[x:]
            x += 1
            y += 1

        if len(adds) >= 300:
            print(-1)
            ok = False
    
    if ok:
        print(len(adds))
        for a in adds:
            print(a, end = " ")
        print()