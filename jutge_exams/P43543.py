
while True:
    parts = input().split("  ")
    maxim = int(parts[0].split(" ")[1])
    nombres = parts[1].split(" ")
    satisfaccions = [int(nombre) for nombre in nombres]
    s = len(satisfaccions)
    F = [satisfaccions[0]]
    seguits = [1]
    minSat = 0

    for i in range(1, min(maxim, s)):
        if satisfaccions[i] < satisfaccions[minSat]:
            minSat = i
        F += [F[-1] + satisfaccions[i]]
        seguits += [seguits[-1] + 1]
    if s <= maxim:
        print(F[-1])
        continue
    if satisfaccions[maxim] < satisfaccions[minSat]:
        minSat = maxim
    F += [F[maxim-1] - satisfaccions[minSat] + satisfaccions[maxim]]
    seguits += [maxim - minSat]
    
    for i in range(maxim + 1, s):
        # Aquí calculem F[i] a partir dels anteriors
        if seguits[i-1] < maxim:
            F += [F[i-1] + satisfaccions[i]]
            seguits += [seguits[i-1] + 1]
            continue         
        optim = F[i-1]
        seguitsOptim = 0
        suma = 0
        for j in range(maxim):
            suma += satisfaccions[i-j]
            if suma + F[i-j-2] > optim:
                optim = suma + F[i-j-2]
                seguitsOptim = j+1
        F += [optim]
        seguits += [seguitsOptim]

    print(F[-1])