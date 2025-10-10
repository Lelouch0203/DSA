def single(nums):
    n=(len(nums)+1)//2
    return n*(n+1)- sum(nums)
def singleBybinary(nums):
    n=len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]
    
    
    l=1 
    r=n-2
    while l<=r:
        mid=(l+r)//2
        if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]) :
            l=mid+1
        else:
           r=mid-1

    return -1
        
print(singleBybinary([1,1,2,3,3,4,4]))
    