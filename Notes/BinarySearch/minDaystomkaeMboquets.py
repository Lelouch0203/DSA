def mboq(n,arr,m,k):
    if m*k>n:
        return -1
    maxi=max(arr)
    mini= min(arr)
    while mini<=maxi:
        mid=(mini+maxi)//2
        if checkflowers(arr,mid,m,k):
            maxi=mid-1
        else:
            mini=mid+1
    return mini 
            
def checkflowers(arr,d,m,k):
    curr=0
    cnt=0
    for b in arr:
        if b<=d:
            curr+=1
        else:
            cnt+=curr//k
            curr=0

    cnt+=curr//k        
    return cnt>=m
    
    
print(mboq(5,[1,10,3,10,2],3,1))
            
                
            
