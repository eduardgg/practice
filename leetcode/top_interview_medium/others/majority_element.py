import collections
import random

def majorityElement(nums):
    counter = 0
    current = None        
    for num in nums:
        if counter == 0:
            current = num    
        if num == current:
            counter += 1
        else:
            counter -= 1
    return current
 
def majorityElement1(nums):
    nums.sort()
    return nums[len(nums)//2]

def majorityElement2(nums):
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)

def majorityElement3(nusms):
    majority_count = len(nums)//2
    while True:
        candidate = random.choice(nums)
        if sum(1 for elem in nums if elem == candidate) > majority_count:
            return candidate

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
nums = [1,1,1,3,3,3,3]
print(majorityElement(nums))
nums = [6,5,5]
print(majorityElement(nums))