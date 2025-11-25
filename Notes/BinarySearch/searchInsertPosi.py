arr= [1,2,4,7]
x=3
def insertt(arr,x):
    l=0
    r=len(arr)-1
    ans=len(arr)
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==x:
            return mid
        if arr[mid]>x:
            ans = mid
            r=mid-1
        else:
            l=mid+1
    
    return ans
    

print(insertt(arr,x))
        