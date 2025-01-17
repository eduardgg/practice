#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        s = set(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                if -arr[i]-arr[j] in s:
                    print(arr[i], arr[j], s)
                    return True
        return False


n = 7
arr = [4, -16, 43, 4, 7, -36, 18]
print(Solution().findTriplets(arr, n))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        if (Solution().findTriplets(a, n)):
            print(1)
        else:
            print(0)

# } Driver Code Ends