
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    pvt=-1
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[i+1]:
            pvt=i
            break
    if pvt==-1:
        nums.reverse()
        return 
    for i in range(len(nums)-1,pvt,-1):
        if nums[i]>nums[pvt]:
            nums[i],nums[pvt]=nums[pvt],nums[i]
            break
    nums[pvt+1:]=reversed(nums[pvt+1:])

    