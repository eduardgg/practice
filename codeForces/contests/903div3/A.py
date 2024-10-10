t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    x = input()
    s = input()

    resultat = -1 
    for j in range(len(x)):
        i = 0
        k = j
        while k < len(x) and i < len(s) and s[i] == x[k]:
            i += 1
            k += 1
        if i == len(s):
            resultat = 0
            break
        if k == len(x):
            totok = True
            for e in range(i, len(s)):
                if s[e] != x[(e-i)%(len(x))]: 
                    totok = False
                    break
            if not totok:
                continue

            ops = 0
            while len(s) > (2**ops)*len(x) - j:
                ops += 1
            resultat = ops
            break
        
        if s[i] != x[k]:
            continue

    print(resultat)