def remoVe(arr):
    m=[]
    for i in arr:
        if i not in m:
            m.append(i)
    return len(m)
# print(remoVe([0, 0, 3, 3, 5, 6]))

def twoP(arr):
    i=0
    j=1
    while i!=len(arr) and j!=len(arr):
        if arr[i]==arr[j]:
            j+=1
        else:
            arr[i+1]=arr[j]
            j+=1
            i+=1
    arr=arr[:i+1]+['_' for i in range(len(arr)-(i+1))]
    return i+1,arr
    
            
print(twoP([0, 0, 3, 3, 5, 6]))  
