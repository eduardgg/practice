
def fpm(v):
    minim = 0
    for i in range(len(v)):
        if v[i] < v[minim]:
            minim = i
    return minim

def f(v):
    i = fpm(v)
    m1 = fpm(v[:i])
    m2 = i+1+fpm(v[i+1:])



t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(f(p))
