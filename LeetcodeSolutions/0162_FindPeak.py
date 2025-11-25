def peak(nums):
    if len(nums)==1:
        return 0
    if nums[0]>nums[1]:
        return 0
    if nums[-1]>nums[-2]:
        return len(nums)-1
    
    l=1
    r=len(nums)-2
        
    while l<=r:
        mid=(l+r)//2
        if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
            return mid
        if nums[mid-1]<nums[mid+1]:
            l=mid+1
        else:
            r=mid-1
    return -1

print(peak([1,2,1,3,5,6,4]))