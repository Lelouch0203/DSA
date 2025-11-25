def minDays( bloomDay, m, k):
    
    def checkflowers(bloomDay,d,m,k):
        curr=0
        cnt=0
        for b in bloomDay:
            if b<=d:
                curr+=1
            else:
                cnt+=curr//k
                curr=0

        cnt+=curr//k        
        return cnt>=m
    
    
    
    n=len(bloomDay)
    if m*k>n:
        return -1
    maxi=max(bloomDay)
    mini= min(bloomDay)
    while mini<=maxi:
        mid=(mini+maxi)//2
        if checkflowers(bloomDay,mid,m,k):
            maxi=mid-1
        else:
            mini=mid+1
    return mini

print(minDays([1,10,3,10,2],3,1))