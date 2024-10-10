
# L'he millorat però tot i així segueix fallant!
# TIME LIMIT EXCEEDED

t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    k = int(input())

    array = [0]*len(c)
    quants = [0]*len(c)
    minim = min(c)
    while minim <= k:
        millor = 0
        cost = c[millor]
        for i in range(len(c)):
            if k//c[i] >= k//c[millor]:
                millor = i
        k -= c[millor]
        quants[millor] += 1
    
    array[-1] = quants[-1]
    for i in range(len(array)-1):
        array[-2-i] = array[-1-i] + quants[-2-i]
    for i in range(len(array)):
        print(array[i], end=" " if i<len(array)-1 else '\n')