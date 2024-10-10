
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    suma = 0
    for i in range(n):
        if a[i] > a[(i+1)%n]:
            suma += 1
    print("Yes" if suma <= 1 else "No")