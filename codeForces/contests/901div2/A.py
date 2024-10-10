t = int(input())
for _ in range(t):
    a, b, n = list(map(int, input().split()))
    x = list(map(int, input().split()))
    resultat = b
    for xi in x:
        resultat += min(a-1, xi)
    print(resultat)