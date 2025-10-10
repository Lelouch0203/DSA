def mininRotated(nums):
    l=0
    r=len(nums)-1
    Min=float("inf")
    while l<=r:
        mid = (l+r)//2
        if nums[l]<nums[mid] and nums[mid]<nums[r]:
            return nums[l] if Min>nums[l] else Min
        else:
            if nums[l]<Min:
                Min=nums[l]
            if nums[r]<Min:
                Min=nums[r]
            l+=1
            r-=1
            print(l,r,Min)
    return Min
print(mininRotated([2,3,4,5,1]))
        