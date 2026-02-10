def gen(open,close,curr,res,n):
    if len(curr)==n*2:
        res.append(curr)
        return 
    if open<n:
        gen(open+1,close,curr+"(",res,n)
    if open>close:
        gen(open,close+1,curr+')',res,n)
    
res = []
gen(0,0,'',res,2)
print(res)