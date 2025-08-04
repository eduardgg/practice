
import heapq

class Solution:

    # Aquesta implementació usa un min heap, que contindrà sempre k+1
    # elements, ja que quan passem per la posició i, l'element correcte
    # haurà d'estar com a molt a la i+k, i tots els altres ja s'hauran
    # anat posant.
    def nearlySorted1(self, arr, k):
        n = len(arr)
        h = []
        for i in range(k+1):
            heapq.heappush(h, arr[i])
        ans = []
        for i in range(k+1, n):
            ans.append(heapq.heappop(h))
            heapq.heappush(h, arr[i])
        while h:
            ans.append(heapq.heappop(h))
        arr[:] = ans

    # Aquesta implementació separa l'array inicial en n/k arrays de longitud k,
    # de manera que podem ordenar cadascuna d'elles per separat i anar-les comparant
    # de 2 en 2 per anar posant sempre l'element menor.
    # S'obtenen n/k arrays de tamany k, que caldrà ordenar totes i fer-hi operacions
    # lineals, per tant el Cost serà O(n/k · kLogk) = O(n · Logk)
    def nearlySorted2(self, arr, k):
        n = len(arr)
        if k >= n:
            arr.sort()
            return
        v1 = arr[:k]
        v2 = arr[k:min(2*k, n)]
        v1.sort(reverse = True)
        v2.sort(reverse = True)
        v = []
        i = 2
        while True:
            while v1 and v2:
                print(i, k, n, v1, v2)
                if v1[-1] < v2[-1]:
                    v.append(v1.pop())
                else:
                    v.append(v2.pop())
            if i*k < n:
                if not v1:
                    v1 = arr[(i*k):min((i+1)*k, n)]
                    v1.sort(reverse = True)
                if not v2:
                    v2 = arr[(i*k):min((i+1)*k, n)]
                    v2.sort(reverse = True)
                i += 1
            else:
                while v1:
                    v.append(v1.pop())
                while v2:
                    v.append(v2.pop())
                break
        arr[:] = v



# { 
# Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        t -= 1

# } Driver Code Ends