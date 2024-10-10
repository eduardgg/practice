# Given an array, rearrange numbers into the
# lexicographically next greater permutation of
# numbers. If such permutation is not possible,
# arrange the elements in lowest possible order.

# Assumim que els nombres són tots positius.
# Recorrem de dreta a esquerra per trobar l'índex
# de menys pes que té un valor inferior a un dels
# de la dreta. Canviarem la seva posició per la del
# menor element que sigui superior a ell (en cas
# d'empat, agafem el de més a la dreta). Un cop
# fet el swap, el subvector que queda a la dreta
# de la primera posició intercanviada està ordenat
# de major a menor, de manera que el podem revertir
# per obtenir la menor seqüència possible.

def next(v):
    max = 0
    pos1 = -1
    for i in range(len(v)):
        if v[len(v)-1-i] >= max:
            max = v[len(v)-1-i]
            continue
        pos1 = len(v)-1-i
        break
    if pos1 == -1:
        v.reverse()
        return v
    pos2 = pos1+1
    for j in range(len(v)-pos1-2):
        if v[pos1+2+j] <= v[pos1]:
            break
        if v[pos1+2+j] <= v[pos2]:
            pos2 = pos1+2+j
    v[pos1], v[pos2] = v[pos2], v[pos1]
    w = v[pos1+1:]
    w.reverse()
    v[pos1+1:] = w
    return v


v = [2,5,7,8,9]
print(next(v))
v = [1,5,8,4,7,6,5,3,1]
print(next(v))
v = [1,5,8,4,7,6,5,5,3,1]
print(next(v))
v = [9,8,7,5,2]
print(next(v))