# Sorting of k-sorted arrays

# Given an unsorted array, with a special property that
# it is not completely sorted: it is a k-sorted array,
# meaning that every element in the array is at a 
# distance almost k from its sorted position.

# Sort the array



def kSorting(v,k,pos):
    if len(v)-pos < 5:
        w = v[pos:]
        w.sort()
        v[pos:] = w
        return
    posmin = pos
    for i in range(k):
        if v[pos+i+1] < v[posmin]:
            posmin = pos+i+1
    v[pos], v[posmin] = v[posmin], v[pos]
    print(v)
    kSorting(v,k,pos+1)
    return

v = [10,9,8,7,4,70,60,50]
k = 4
kSorting(v,k,0)
print(v)