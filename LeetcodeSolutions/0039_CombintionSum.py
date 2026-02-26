def combinationSum(candidates, target):
    res = []
    curr= []
    candidates.sort()
    def btk(strt,target):
        if target==0:
            res.append(curr[:])
            return 
        for i in range(strt,len(candidates)):
            if candidates[i]>target:
                break
            curr.append(candidates[i])
            btk(i,target-candidates[i])
            curr.pop()
    btk(0,target)
    return res

print(combinationSum([2,3,6,7],7))