
for _ in range(int(input())):
    n = int(input())
    a = input()
    uns = int(a[0])
    cons = False
    for i in range(1, n):
        uns += int(a[i])
        if int(a[i]) and int(a[i-1]):
            cons = True
    if uns%2 or (uns == 2 and cons):
        print("NO")
    else:
        print("YES")        