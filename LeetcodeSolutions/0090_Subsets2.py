def subsetsWithDup(nums):
    res = []
    nums.sort()
    curr = []
    def bkt(strt):
        res.append(curr[:])
        for i in range(strt,len(nums)):
            if i > strt and nums[i]==nums[i-1]:
                continue
            curr.append(nums[i])
            bkt(i+1)
            curr.pop()
    bkt(0)
    return res
print(subsetsWithDup([0]))