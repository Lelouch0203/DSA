res = []
def comb(strt,arr,curr):
    if strt == len(arr):
        res.append(curr[:])
        return
    comb(strt+1,arr,curr)
    curr.append(arr[strt])
    comb(strt+1,arr,curr)
    curr.pop()
comb(0,[1,2,3],[])
print(res)
    