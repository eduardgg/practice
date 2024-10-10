class Solution(object):
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

    def longestConsecutive2(self, nums):
        nums.sort()
        current = nums[0]
        streak = 1
        maxim = 1
        for num in nums[1:]:
            if num == current:
                continue
            elif num == current + 1:
                streak += 1
            else:
                streak = 1
            current = num
            if streak > maxim:
                maxim = streak
        return maxim

sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [100,4,200,1,3,2]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(sol.longestConsecutive(nums))
print(sol.longestConsecutive2(nums))