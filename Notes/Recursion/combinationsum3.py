def comb(n, target):
    res = []
    curr = []
    def bkt(strt,target):
        if target==0 and len(curr)==n:
            res.append(curr.copy())
            return 
        for i in range(strt,10):
            if len(curr)>n:
                break
            if target<0:
                break
            curr.append(i)
            bkt(i+1,target-i)
            curr.pop()
    bkt(1,target)
    return res
print(comb(3,9))