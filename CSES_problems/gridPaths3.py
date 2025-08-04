
# Aplicant backtracking directe, dura 875,1 s 
# Gràcies a aquesta funció, l'execució baixa a 23.8 s
# La comprovació de not used[0][6] abans d'hora ho millora a 11.5 s
# La comprovació de cel·les vàlides (allValid) redueix a 5.4 s

s = input()
used = [[False for _ in range(7)] for _ in range(7)]
ans = 0



def f(x, y, k):

    global ans
    if k == 48:
        if x == 0 and y == 6:
            ans += 1
        return

    if used[0][6]: return

    if (x == 0 or used[x-1][y]) and (x == 6 or used[x+1][y]):
        if 0 < y < 6 and not used[x][y-1] and not used[x][y+1]:
            return
    if (y == 0 or used[x][y-1]) and (y == 6 or used[x][y+1]):
        if 0 < x < 6 and not used[x-1][y] and not used[x+1][y]:
            return
        
    used[x][y] = True
    if s[k] in "L?" and x > 0 and not used[x-1][y]:
        f(x-1, y, k+1)
    if s[k] in "R?" and x < 6 and not used[x+1][y]:
        f(x+1, y, k+1)
    if s[k] in "U?" and y > 0 and not used[x][y-1]:
        f(x, y-1, k+1)
    if s[k] in "D?" and y < 6 and not used[x][y+1]:
        f(x, y+1, k+1)
    used[x][y] = False


f(0, 0, 0)
print(ans)

# Input: ??????R??????U??????????????????????????LD????D?
# Output: 201

# Input: ????????????????????????????????????????????????
# Output: 88418
