
t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    k = 2
    while True:
        n1 = v[0] % k
        n2 = None
        valid = True
        for i in range(1, len(v)):
            if v[i] % k != n1:
                if n2 == None:
                    n2 = v[i] % k
                elif v[i] % k == n2:
                    continue
                else:
                    valid = False
                    break
        if valid and n2 != None:
            print(k)
            break
        
        # La clau de tot plegat:
        k *= 2