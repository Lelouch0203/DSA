def search(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        print(l,r)
        mid=(l+r)//2

        if nums[mid]==target:
            return True
        if nums[mid]==nums[l] and nums[l]==nums[r] :
            l+=1
            r-=1
            continue
        if nums[mid]<=nums[r]:
            if nums[mid]<=target and nums[r]>=target:
                l=mid+1
            else:
                r=mid-1
        else:
            if nums[l]<=target and nums[mid]>=target:
                r=mid-1
            else:
                l=mid+1
                
    return False

print(search([3,3,0,1,2,3,3,3,3,3,3,3,3],0))
              