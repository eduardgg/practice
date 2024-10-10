t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    atacs = 0
    counter = 0
    posl = 0
    posr = len(a) - 1
    while posl < posr:
        if counter + a[posl] >= a[posr]:
            a[posl] -= (a[posr] - counter)
            atacs += a[posr] - counter + 1
            counter = 0
            posr -= 1
        else:
            atacs += a[posl]
            counter += a[posl]
            posl += 1

    if counter > a[posl]:
        print("WTF")
    elif a[posl] == 0:
        print(atacs)
    elif a[posl] == 1:
        atacs += 1
        print(atacs)
    elif counter == 0:
        atacs += (a[posr] + 3) // 2
        print(atacs)
    else:
        atacs += (a[posr] - counter + 1) // 2 + 1
        print(atacs)