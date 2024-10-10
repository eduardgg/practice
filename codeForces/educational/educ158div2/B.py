t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    resultat = c[0] - 1
    for i in range(len(c)-1):
        resultat += max(0, c[i+1]-c[i])
    print(resultat)