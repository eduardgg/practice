
# Fet amb backtracking, resposta incorrecta igualment. Mal plantejat.

def neteja():
    maxv = len(s)
    minv = 1
    for i in range(len(s)):
        if s[-1-i] == '>':
            nombres[-1-i] = maxv
            usat[maxv-1] = True
            maxv -= 1
        elif s[-1-i] == '<':
            nombres[-1-i] = minv
            usat[minv-1] = True
            minv += 1
    maa[0] = maxv + 1
    mii[0] = minv - 1


def f(i):
    
    if i == n:
        print(nombres)
        print(s)
        return 1
    
    sum = 0
    
    if i == 0:
        for j in range(mii[0]+1, maa[0]):
            nombres[i] = j
            usat[j-1] = True
            minim[0] = j
            maxim[0] = j
            sum += f(1)
            usat[j-1] = False
        return sum

    elif s[i] == '<':
        if nombres[i] >= minim[0]:
            return 0
        minim[0] = nombres[i]
        return f(i+1)

    elif s[i] == '>':
        if nombres[i] <= maxim[0]:
            return 0
        maxim[0] = nombres[i]
        return f(i+1)

    elif s[i] == '?':
        for j in range(minim[0]+1, maxim[0]):
            if usat[j-1]:
                continue
            nombres[i] = j
            usat[j-1] = True
            prevMax = maxim[0]
            prevMin = minim[0]
            maxim[0] = max(maxim[0], j)
            minim[0] = min(minim[0], j)
            sum += f(i+1)
            maxim[0] = prevMax
            minim[0] = prevMin
            usat[j-1] = False
        return sum
    

n, m = list(map(int, input().split()))
s = '?' + input()

maa = [-1]
mii = [-1]
maxim = [float('-inf')]
minim = [float('inf')]
usat = [False]*n
nombres = [-1]*n
neteja()
print(f(0))

for _ in range(m):
    i, c = input().split()
    i = int(i)
    s = s[:i] + c + s[i+1:]
    for i in range(10):
        print(i, end="  ")
    for i in range(10, 30):
        print(i, end=" ")
    print()
    for e in s:
        print(e, end="  ")
    print()

    maa = [-1]
    mii = [-1]
    maxim = [float('-inf')]
    minim = [float('inf')]
    usat = [False]*n
    nombres = [-1]*n
    # neteja()
    # print(f(0))