def ipLb(arr,x):
    l=0
    r=len(arr)-1
    ans=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>=x:
            ans=mid
            r=mid-1
            
        else:
            l=mid+1
    return ans
print(ipLb([5,7,7,8,8,10],8))   
