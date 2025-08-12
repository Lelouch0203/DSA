def push_zeros(arr):
    nonzero=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[nonzero],arr[i]=arr[i],arr[nonzero]
            nonzero+=1
            
    return arr
# print(push_zeros([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))
def moveZeros(a,n):
    j = -1
    # Place the pointer j
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    
    # No non-zero elements
    if j == -1:
        return a
    
    # Move the pointers i and j and swap accordingly
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    
    return a
print(moveZeros([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1],8))