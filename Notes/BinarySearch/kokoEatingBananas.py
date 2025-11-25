import time
import math
def caluculateTotalHours(arr,hourly):
    t=0
    for i in arr:
        t+=math.ceil(i/hourly)
    return t
def minRate(arr,h):
    maxi=max(arr)
    for i in range(1,maxi+1):
        reqtime=caluculateTotalHours(arr,i)
        if reqtime<=h:
            return i
    
    
    return maxi
            
v = [25, 12, 8, 14, 19]
h = 5
# start=time.time()
# ans= minRate(v,h)
# print("Koko should eat at least", ans, "bananas/hr.")
# end=time.time()
# print(end-start)


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
start=time.time()
ans = usingBin(v, h)

print("Koko should eat at least", ans, "bananas/hr.")
end=time.time()
print(end-start)
