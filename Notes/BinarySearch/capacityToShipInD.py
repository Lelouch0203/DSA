def check(arr,cp):
    days=1
    currwt=0
    for wt in arr:
        currwt+=wt
        if currwt>cp:
            days+=1
            currwt=wt
    return days
def capcty(arr,d):
    l=max(arr)
    r=sum(arr)
    while l<=r:
        mid =(l+r)//2
        print(l,mid,r)
        if check(arr,mid)<=d:
            r=mid-1
        else:
            l=mid+1
            
    return l


print(capcty([5,4,5,2,3,4,5,6],5))