def canFinish(numCourses, prerequisites):

    n = numCourses
    labels = [0]*n
    currentLabel = 1

    # Diccionari de requisits de cada curs:
    reqs = {}
    for v in prerequisites:
        reqs[v[0]] = reqs.get(v[0],[]) + [v[1]]
    
    # Diccionari invers a l'anterior:
    inv = {}
    for i in range(n):
        for j in reqs.get(i,[]):
            inv[j] = inv.get(j,[]) + [i]

    # Trobem el vector que indica el nombre de previs
    # que requereix cada curs. Més endavant, li restarem
    # 1 a la posició corresponent cada cop que s'hagi
    # complert un dels requeriments. Quan arribi a 0,
    # l'afegirem al vector de sinks (pous), disponibles
    # per cursar actualment.
    previs = []
    sinks = []
    for i in range(n):
        previs.append(len(reqs.get(i,[])))
        if previs[i] == 0:
            sinks.append(i)
    
    # Comencem la solució "recursiva". A cada iteració,
    # mirem si hi ha pous. Si és així, el marquem en
    # l'ordre actual, i si no retornem False.
    # Quan haguem acabat, si hem pogut donar un ordre a
    # totes les activitats, retornem True.
    for i in range(n):
        if len(sinks) == 0:
            return False
        sink = sinks.pop()
        labels[sink] = currentLabel
        currentLabel += 1
        for j in inv.get(sink,[]):
            previs[j] -= 1
            if previs[j] == 0:
                sinks.append(j)

    # print(labels)
    order = [0]*n
    for i in range(n):
        order[labels[i]-1] = i+1
    print(order)
    return True



numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))

numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(canFinish(numCourses, prerequisites))

numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]
print(canFinish(numCourses, prerequisites))

numCourses = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
print(canFinish(numCourses, prerequisites))