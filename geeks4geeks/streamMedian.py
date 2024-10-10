
# Update the median of an array, streaming the values

# Given the first m numbers,
# h1 is a max heap storing the smallest m//2 values,
# and h2 is a min heap storing the largest ones.
# As we keep streaming the array's values, we insert
# them in the heaps to keep them balanced (with a
# difference of sizes <= 1), and then simply output
# the median, which will either be the maximum of h1,
# or the minimum of h2, needing only a heappop.

# Total time complexity: O(n·logn)
# Total space complexity: O(n)


from heapq import heappop, heappush

h1, h2 = [], []

n = int(input())

for _ in range(n):

    m = int(input())
    
    if h2 and m <= h2[0]:
        heappush(h1, -m)
    else:
        heappush(h2, m)

    if len(h1) > len(h2)+1:
        heappush(h2, -heappop(h1))
    elif len(h2) > len(h1):
        heappush(h1, -heappop(h2))
    
    print(-h1[0])