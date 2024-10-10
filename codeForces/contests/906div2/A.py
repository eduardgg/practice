t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    num1 = v.pop()
    count1 = 1
    num2 = None
    count2 = 0
    ok = True
    for e in v:
        if e != num1 and num2 == None:
            num2 = e
            count2 += 1
            continue
        if e == num1:
            count1 += 1
        elif e == num2:
            count2 += 1
        else:
            ok = False
            break
    if not ok:
        print("NO")
        continue
    if count2 == 0 or count1 - count2 in [-1,0,1]:
        print("YES")
    else:
        print("NO")