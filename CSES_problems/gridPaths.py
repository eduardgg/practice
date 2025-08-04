
# Aplicant backtracking directe, dura 875,1 s 
# Gràcies a aquesta funció, l'execució baixa a 23.8 s
# La comprovació de not used[0][6] abans d'hora ho millora a 11.5 s
# La comprovació de cel·les vàlides (allValid) redueix a 5.4 s

# s = input()
# s = '?'*48
s = "??????R??????U??????????????????????????LD????D?"

used = [[False for _ in range(7)] for _ in range(7)]
used[0][0] = True
ans = 0

def disconnected():
    primera = False
    vist = [row[:] for row in used]
    for i in range(7):
        for j in range(7):
            if not vist[i][j]:
                if primera:
                    return True
                primera = True
                stack = [(i, j)]
                vist[i][j]
                while stack:
                    x, y = stack.pop()
                    if x > 0 and not vist[x-1][y]:
                        stack.append((x-1, y))
                        vist[x-1][y] = True
                    if x < 6 and not vist[x+1][y]:
                        stack.append((x+1, y))
                        vist[x+1][y] = True
                    if y > 0 and not vist[x][y-1]:
                        stack.append((x, y-1))
                        vist[x][y-1] = True
                    if y < 6 and not vist[x][y+1]:
                        stack.append((x, y+1))
                        vist[x][y+1] = True
    return False


def allValid(i, j):
    for x in range(6):
        for y in range(6):
            if not used[x][y] and (x, y) != (0, 6) and (x-i)*(x-i)+(y-j)*(y-j) != 1:
                cnt = 0
                if x > 0 and not used[x-1][y]: cnt += 1
                if x < 6 and not used[x+1][y]: cnt += 1
                if y > 0 and not used[x][y-1]: cnt += 1
                if y < 6 and not used[x][y+1]: cnt += 1
                if cnt < 2:
                    return False
    return True



def f(x, y, k):

    global ans
    if k == 48:
        if x == 0 and y == 6:
            ans += 1
        return

    if k < 48 and used[0][6]: return
    if disconnected(): return
    if not allValid(x, y): return
    
    if s[k] in "L?" and x > 0 and not used[x-1][y]:
        used[x-1][y] = True
        f(x-1, y, k+1)
        used[x-1][y] = False
    if s[k] in "R?" and x < 6 and not used[x+1][y]:
        used[x+1][y] = True
        f(x+1, y, k+1)
        used[x+1][y] = False
    if s[k] in "U?" and y > 0 and not used[x][y-1]:
        used[x][y-1] = True
        f(x, y-1, k+1)
        used[x][y-1] = False
    if s[k] in "D?" and y < 6 and not used[x][y+1]:
        used[x][y+1] = True
        f(x, y+1, k+1)
        used[x][y+1] = False


f(0, 0, 0)
print(ans)

# Input: ??????R??????U??????????????????????????LD????D?
# Output: 201

# Input: ????????????????????????????????????????????????
# Output: 88418
