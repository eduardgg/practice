
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    suma = 0
    vists = {0}
    trobat = False
    for i in range(len(a)):
        if i%2 == 0:
            a[i] = -a[i]
        suma += a[i]
        if suma in vists:
            print("YES")
            trobat = True
            break
        vists.add(suma)
    
    if not trobat:
        print("NO")