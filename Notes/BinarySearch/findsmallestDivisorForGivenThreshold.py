import math
def divcheck(arr,div):
    Sum=0
    for num in arr:
        Sum+=math.ceil(num/div)
    return Sum
def smolDiv(arr,lim):
    if len(arr)>lim:
        return -1
    l=1
    r=max(arr)
    
    while l<=r:
        mid=(l+r)//2
        if divcheck(arr,mid)<=lim:
            r=mid-1
        else:
            l=mid+1
    return l
print(smolDiv([8,4,2,3],10))