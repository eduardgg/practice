n = int(input())
a = list(map(int, input().split()))

minim = float('inf')
maxEsq = [0]*n
maxDre = [0]*n

for i in range(len(a)-1):
    maxEsq[i+1] = max(maxEsq[i], a[i]+(n-1-i))
    maxDre[-2-i] = max(maxDre[-1-i], a[-1-i]+(n-1-i))

for i in range(len(a)):
    pitjor = max(a[i], maxEsq[i], maxDre[i])
    if pitjor < minim:
        minim = pitjor

print(minim)