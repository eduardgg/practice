def lis(array):
    dp = [0]*(len(array))   
    minim = 10000
    for i in range(len(array)):
        if array[i] <= minim:
            minim = array[i]
            dp[i] = 1
        else:
            dp[i] = 1 + max(dp[j] for j in range(0,i) if array[j] < array[i])
    return max(dp[i] for i in range(len(dp)))

nums = [10,9,2,5,3,7,101,18]
print (lis(nums))

nums = [0,1,0,3,2,3]
print (lis(nums))