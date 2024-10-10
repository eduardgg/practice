def f(nums, ans, v, i):
    if i == len(nums):
        ans.append([nums[i] for i in range(len(nums)) if v[i] == 1])
        return
    v.append(0)
    f(nums,ans,v,i+1)
    v.pop(len(v)-1)
    v.append(1)
    f(nums,ans,v,i+1)
    v.pop(len(v)-1)
    return ans

nums = [1,2,3]
print(f(nums,[],[],0))
nums = [5]
print(f(nums,[],[],0))
nums = [0,1]
print(f(nums,[],[],0))