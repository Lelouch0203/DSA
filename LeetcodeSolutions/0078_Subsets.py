def subsets(nums):
    res = []
    def bkt(strt,curr):
        res.append(curr[:])
        for i in range(strt,len(nums)):
            curr.append(nums[i])
            bkt(i+1,curr)
            curr.pop()

    bkt(0,[])
    return res
print(subsets([1,2,4]))
            
        