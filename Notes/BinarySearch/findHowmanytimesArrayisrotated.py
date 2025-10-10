def check(nums):
    l=0
    r=len(nums)-1
    cnt=0
    while l<=r:
        mid=(l+r)//2
        if nums[mid]<nums[r] and nums[l]<nums[mid]:
            return cnt
        else:
            cnt+=1
            l+=1
            r-=1
    return cnt

print(check([4, 5, 6, 7, 0, 1, 2, 3]))