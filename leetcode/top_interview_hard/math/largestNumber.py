
class Solution(object):

    def largestNumber(self, nums):
        
        def greater(x, y):
            x, y = str(x), str(y)
            minl = min(len(x), len(y))
            for i in range(minl):
                if int(x[i]) > int(y[i]):
                    return True
                elif int(x[i]) < int(y[i]):
                    return False
            if len(x) == len(y):
                return True
            elif len(x) > len(y):
                return greater(x[len(y):], y)
            else:
                return greater(x, y[len(x):])

        def qSort(L):
            return L if len(L) <= 0 else (
                qSort([x for x in L[1:] if not greater(x,L[0])]) + 
                L[0:1] + 
                qSort([x for x in L[1:] if greater(x,L[0])])
            )

        L = qSort(nums)
        L.reverse()
        s = ""
        for e in L:
            s = s + str(e)
        primer = -1
        for i in range(len(s)):
            if s[i] != "0":
                primer = i
                break
        if primer == -1:
            return "0"
        return s[primer:]


sol = Solution()
nums = [3,30,34,5,9]
print(sol.largestNumber(nums))
nums = [34323,3432]
print(sol.largestNumber(nums))
nums = [0,0]
print(sol.largestNumber(nums))
nums = [1,2,3,4,5,6,7,8,9,0]
print(sol.largestNumber(nums))