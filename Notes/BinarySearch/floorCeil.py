def floorCeil(arr,k):
    l = 0
    r = len(arr)-1
    ans= len(arr)
    while l <=r:
        mid = (l+r)//2
        if arr[mid]==k:
            return arr[mid],arr[mid]
        if arr[mid]>k:
            
            ans=mid
            r=mid-1
        else:
            l=mid+1
            
    return arr[ans-1],arr[ans]
print(floorCeil([3,4,4,7,8,10],5))