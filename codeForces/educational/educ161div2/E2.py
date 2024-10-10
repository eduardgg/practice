 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    X = int(input())
    v = []
    maxim = 100
    n = X.bit_length()
    X -= 2**(n-1)
    v = [i for i in range(n-1)]

    i = 1
    while X > 0:
        if X >= 2**(n-i-1):
            v.append(v[n-i-1])
            X -= 2**(n-i-1)
        i += 1

    print(len(v))
    for e in v:
        print(e, end=" ")
    print()