
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    s = input()
    if int(s[:2]) == 0:
        print("12" + s[2:] + " AM")
    elif int(s[:2]) == 12:
        print(s + " PM")
    elif int(s[:2]) > 12:
        hora = str(int(s[:2])-12)
        if len(hora) == 1:
            hora = '0' + hora
        print(hora + s[2:] + " PM")
    else:
        print(s + " AM")