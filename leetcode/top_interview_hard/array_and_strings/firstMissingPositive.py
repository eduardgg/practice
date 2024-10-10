class Solution(object):
    def firstMissingPositive(self, nums):
        S = set()
        for num in nums:
            if num > 0:
                S.add(num)
        for i in range(len(S)+1):
            if i+1 not in S:
                return i+1