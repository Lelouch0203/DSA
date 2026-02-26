def comb(arr,i,k,curr,res):
    if i == len(arr) or k <0:
        return 
    if k == 0:
        res.append(curr[:])
        return 
    curr.append(arr[i])
    comb(arr,i,k-arr[i],curr,res)
    curr.pop()
    comb(arr,i+1,k,curr,res)
res = []

comb([2,3,5],0,8,[],res)
print(res)

