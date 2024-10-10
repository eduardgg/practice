class Solution(object):
    def findDuplicate(self, nums):
        S = set()
        for num in nums:
            if num in S:
                return num
            S.add(num)