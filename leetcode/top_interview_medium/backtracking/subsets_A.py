def subsets(nums):
    if len(nums) == 0:
        return [[]]
    answer = []
    S = subsets(nums[0:len(nums)-1])
    for i in range(len(S)):
        answer.append(S[i])
    for i in range(len(S)):
        answer.append(S[i] + [nums[len(nums)-1]])
    return answer

nums = [1,2,3]
print(subsets(nums))
nums = [5]
print(subsets(nums))
nums = [0,1]
print(subsets(nums))