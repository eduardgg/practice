"""
AGGRCOW - Aggressive cows (binary-search)

Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls.
The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).
His C (2 <= C <= N) cows don't like this barn layout and become aggressive
towards each other once put into a stall. To prevent the cows from hurting each other,
FJ wants to assign the cows to the stalls, such that the minimum distance between any
two of them is as large as possible. What is the largest minimum distance?

INPUT: Number of cows to locate and integer array of stall locations.
OUTPUT: The largest minimum distance between cows.
"""

def minDistance(cows, stalls):
    stalls.sort()
    result = 1
    low = stalls[0]
    high = stalls[len(stalls) - 1]
    while low <= high:
        mid = (high + low) // 2
        if good(mid, cows, stalls):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

def good(mid, cows, stalls):
    count = 1
    pos = 0
    for i in range(len(stalls)-1):
        if stalls[i+1] >= stalls[pos] + mid:
            count += 1
            pos = i+1
        if count == cows:
            return True
    return False

def locations(cows, stalls, dist):
    count = 1
    pos = 0
    v = [stalls[pos]]
    for i in range(len(stalls)-1):
        if stalls[i+1] >= stalls[pos] + dist:
            count += 1
            pos = i+1
            v.append(stalls[pos])
        if count == cows:
            return v

cows = 3
stalls = [4,9,8,2,1]
dist = minDistance(cows, stalls) 
print(dist)
print(locations(cows, stalls, dist))