def check(nums):
    if nums==sorted(nums):
        return True
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            nums=nums[i+1:]+nums[:i+1]
            return  (nums == sorted(nums))
print(check(nums=[3,4,5,1,2]))
