def splitt(arr,k):
    l=max(arr)
    r=sum(arr)
    while l<=r:
        mid=(l+r)//2
        if countSize(arr,mid)<=k:
            r=mid-1
        else:
            l=mid+1
    return l
             
def countSize(arr,maxi):
    parts=1
    currsum = 0 
    for i in arr:
        currsum+=i
        if currsum>maxi:
            currsum=i
            parts+=1
    return parts

print(splitt([1,2,3,4,5],3))