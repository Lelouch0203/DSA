def combinationSum3(k,n):
    res = []
    curr = []
    def btk(strt,target):
        if target == 0 and len(curr)==k:
            res.append(curr[:])
            return
        if len(curr)>=k or target<0:
            return 
        for i in range(strt,10):
            if i>target:
                break
            curr.append(i)
            btk(i+1,target-i)
            curr.pop()
    btk(1,n)
    return res
print(combinationSum3(3,7))