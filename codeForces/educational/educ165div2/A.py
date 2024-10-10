
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ok = False
    for i in range(n):
        if i+1 == a[a[i]-1]:
            ok = True
            break
    if ok == True:
        print(2)
    else:
        print(3)