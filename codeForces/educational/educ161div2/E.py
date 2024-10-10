
mi = lambda :map(int,input().split())
li = lambda :list(mi())

# Aquest mètode està bé però el vector surt massa llarg
for _ in range(int(input())):
    X = int(input())
    v = []
    maxim = 100
    while X > 1:
        n = X.bit_length()
        X -= 2**(n-1)-1
        v += [i for i in range(maxim+2-n, maxim+1)]
        maxim = maxim+1-n
    print(len(v))
    for e in v:
        print(e, end=" ")
    print()