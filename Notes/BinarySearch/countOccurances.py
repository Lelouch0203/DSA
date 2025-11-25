def CoS(nums,target):
    l=0 
    r=len(nums)-1
    ans=len(nums)
    while l<=r:
        mid = (l+r)//2
        if nums[mid]>target:
            r=mid-1
            ans=mid
        else:
            l=mid+1
    l =0 
    r= len(nums)-1
    ans2=len(nums)
    while l<=r:
        mid = (l+r)//2
        if nums[mid]>=target:
            r=mid-1
            ans2=mid
        else:
             l=mid+1    
    print(ans,ans2)
             
    return ans-ans2
print(CoS([2,2,3,3,3,3,4],3))
        
    