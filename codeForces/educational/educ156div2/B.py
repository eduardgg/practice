t = int(input())
for _ in range(t):
    Px, Py = list(map(int, input().split()))
    Ax, Ay = list(map(int, input().split()))
    Bx, By = list(map(int, input().split()))

    
    distPA = ((Px-Ax)**2+(Py-Ay)**2)**0.5
    distPB = ((Px-Bx)**2+(Py-By)**2)**0.5
    distAB = ((Bx-Ax)**2+(By-Ay)**2)**0.5
    distP = (Px**2+Py**2)**0.5
    distA = (Ax**2+Ay**2)**0.5
    distB = (Bx**2+By**2)**0.5

    if distPA <= distPB and distA <= distB:
        print(max(distPA, distA))
        continue
    elif distPA > distPB and distA > distB:
        print(max(distPB, distB))
        continue
    elif distPA <= distPB and distA > distB:
        r = max(distB, distPA, distAB/2)
        print(r)
        continue
    else:
        r = max(distA, distPB, distAB/2)
        print(r)
        continue