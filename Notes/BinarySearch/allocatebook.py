def allocate(arr,m):
    l=max(arr)
    r=sum(arr)
    while l<=r:
        mid = (l+r)//2
        if countstudents(arr,mid)<=m:
            r=mid-1
        else:
            l=mid+1
    return l
            
def countstudents(arr,maxpages):
    students=1
    currpages=0

    for pages in arr:   
        currpages+=pages
        if currpages>maxpages:
            currpages=pages
            students+=1
    return students
            
print(allocate([25, 46, 28, 49, 24],3))
