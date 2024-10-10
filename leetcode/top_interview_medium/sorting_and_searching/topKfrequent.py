def topKfrequent(nums, k):
    dic = {}
    for n in nums:
        dic[n] = dic.get(n,0) + 1
    quants = [dic[i] for i in dic.keys()]
    quants.sort()

    if len(quants) <= k:
        return [i for i in dic.keys()]
    
    # Trobem l'invers del diccionari:
    inv = {}
    for n in dic.keys():
        inv[dic[n]] = inv.get(dic[n],[]) + [n]

    output = []
    for i in range(k):
        q = quants.pop()
        element = inv[q].pop()
        output += [element]
    return output

nums = [1,1,1,1,2,2,3,4,4,4,4,5,5,5]
k = 3
print(topKfrequent(nums, k))

nums = [1,2]
k = 2
print(topKfrequent(nums, k))

nums = []
k = 4
print(topKfrequent(nums, k))

nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKfrequent(nums, k))