# using two loops
def countfreq(arr,n):
    visited=[False]*n
    for i in range(n):
        if visited==True:
            continue   
        count=1     
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                count+=1
                visited[j]==True
        print(arr[i],count) 
        
# using hashmap
def countfreqhash(arr):
    m={}
    for i in range(len(arr)):
        if arr[i] in m:
            m[arr[i]]+=1
        else:
            m[arr[i]]=1
    for x in m:
        print(x, m[x],end=" ")
countfreqhash(arr = [10,5,10,15,10,5])


# simpler way
def count3(arr):
    m={}
    for i in arr:
        if i in m:
            m[i]+=1
        else:
            m[i]=1
    for x in m:
        print(x,m[x],end=" ")
count3(arr = [10,5,10,15,10,5])
print()

# heck method
def count4(arr):
    m={}
    for x in arr:
       m[x]=m.get(x,0)+1
    for x in m:
        print(x,m[x],end=" ")
count4(arr = [10,5,10,15,10,5])


