
def f(k, perm):
    if k == 0:
        concatenacio = ""
        for i in perm:
            concatenacio += strings[i]
        print(concatenacio)
        return True
    for i in range(len(strings)):
        if usat[i]:
            continue
        if k < len(strings):
            if strings[i][0] == strings[perm[-1]][-1]:
                continue
        perm += [i]
        usat[i] = True
        if f(k-1, perm):
            return True
        perm.pop()
        usat[i] = False
    return False

while True:
    linia = input().split(" ")
    strings = linia[1:]
    strings.sort()
    s = len(strings)
    perm = []
    usat = [False]*s
    if not f(s, perm):
        print("NO")
        continue