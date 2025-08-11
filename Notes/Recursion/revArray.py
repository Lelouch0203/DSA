def revarr(arr,l,r):
    if l>r:
        return arr
    arr[l],arr[r] = arr[r],arr[l]
    return revarr(arr,l+1,r-1)
print(revarr([1,2,3,4],0,3))

def revArr(arr,i,n):
    if i>=n/2:
        return arr
    arr[i],arr[n-1-i]=arr[n-i-1],arr[i]
    return revArr(arr,i+1,n)
print(revArr([1,2,3,4],0,4))