def miss(arr,k):
    # for num in arr:
    
    #     if num<=k:
    #         k+=1
    #     else :
    #        return k
    # return k
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        missing=arr[mid]-(mid+1)
        print(missing)
        if missing<k:
            l=mid+1
        else:
            r=mid-1
        print(l,r,mid)
    return l+k
            
print(miss([2,3,4,7,11],3))


