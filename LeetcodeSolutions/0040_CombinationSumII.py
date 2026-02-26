def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    curr= []
    def bkt(strt,target):
        if target==0:
            res.append(curr.copy())
            return 
        for i in range(strt,len(candidates)):
            if candidates[i]==candidates[i-1] and i>strt:
                continue
            if candidates[i]>target:
                break
            curr.append(candidates[i])
            bkt(strt+1,target-candidates[i])
            curr.pop()
    bkt(0,target)
    return res    
print(combinationSum2([1,2,2,3],4))
