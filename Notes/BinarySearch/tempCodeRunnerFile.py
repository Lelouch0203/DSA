l=0
    r=len(nums)-1
    Min=float("inf")
    while l<=r:
        mid = (l+r)//2
        if nums[mid]<Min:
            Min=nums[mid]
        if nums[l]<nums[r]:
            r=mid-1
        else:
            l=mid+1
    return Min