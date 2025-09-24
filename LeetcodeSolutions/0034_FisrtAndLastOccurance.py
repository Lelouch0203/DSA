def fnLo(nums,target):
    l=0
    r=len(nums)-1
    res=[]
    ans=len(nums)
    
    while l<=r:
        mid = (l+r)//2

        if nums[mid]>=target:
            ans = mid
            r=mid-1
        else:
            l=mid+1
    if nums[ans-1]!=target:
        return [-1,-1]
    
    res.append(ans)
    
    
    l=0
    r=len(nums)-1
    ans=len(nums)
    
    while l<=r:
        mid=(l+r)//2
        if nums[mid]>target:
            r=mid-1
            ans=mid
        else:
            l=mid+1
            
   
    res.append(ans-1)
            
    return res

print(fnLo([1,2,3],6))