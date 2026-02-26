res = []
def comb(start,path,arr,target):
    if target == 0:
        res.append(path.copy())
        return
    for i in range(start,len(arr)):
        if i > start and arr[i]==arr[i-1]:
            continue
        if arr[i]>target:
            break
        path.append(arr[i])
        comb(start+1,path,arr,target-arr[i])
        path.pop()
comb(0,[],[1,1,2,2,4],4)
print(res)

    