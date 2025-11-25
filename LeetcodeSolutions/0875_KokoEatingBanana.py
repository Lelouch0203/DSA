import math
def usingBin(arr,h):
    l=1
    r=max(arr)+1
    while(l<=r):
        mid=(l+r)//2
        reqtime=caluculateTotalHours(arr,mid)
        if reqtime<=h:
            r=mid-1
     
        else:
            l=mid+1
    return l
def caluculateTotalHours(arr,hourly):
    t=0
    for i in arr:
        t+=math.ceil(i/hourly)
    return t    
v = [25, 12, 8, 14, 19]
h = 5
print(usingBin(v, h))