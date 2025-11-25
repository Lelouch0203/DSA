def minMax(arr,k):
    howmany=[0]*(len(arr)-1)
    for _ in range(1,k+1):
        maxSection=-1
        maxIdx=-1
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            sectionLen = diff/(howmany[i]+1)
            if sectionLen>maxSection:
                maxSection=sectionLen
                maxIdx=i
        howmany[maxIdx]+=1
        
    maxAns=-1
    for i in range(len(arr)-1):
        diff = arr[i+1]-arr[i]
        sectionLen = diff/(howmany[i]+1)
        maxAns=max(maxAns,sectionLen)
    return maxAns


arr = [1,2,3,4,5]
k = 4
ans = minMax(arr, k)
print("The answer is:", ans)


def numofgasdtsionsreq(dist,arr):
    n=len(arr)
    cnt=0
    for i in range(1,n):
        numberInBtw=((arr[i]-arr[i-1])/dist)
        if ((arr[i]-arr[i-1])==(dist*numberInBtw)):
            numberInBtw-=1
        cnt+=numberInBtw

    return cnt
def mininmiseMaxDist(arr,k):
    n=len(arr)
    low=0
    high = 0
    
    for i in range(n-1):
        high=max(high,arr[i+1]-arr[i])

    diff =1e-6
    while high-low>diff:
        mid= (low+high)/2.0
        cnt=numofgasdtsionsreq(mid,arr)
        if cnt>k:
            low=mid
        else:
            high=mid
            
    return high

print(mininmiseMaxDist(arr,k))