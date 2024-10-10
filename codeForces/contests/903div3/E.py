
# Sembla correcte i eficient, però:
# Runtime error on test 4/5

def f(i):
    if i == n:
        return 0
    if F[i] != -1:
        return F[i]
    F[i] = 1 + f(i+1)
    if i+v[i] < n:
        F[i] = min(F[i], f(i+v[i]+1))
    return F[i]

t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    F = [-1]*n
    print(f(0))