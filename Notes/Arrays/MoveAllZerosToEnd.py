arr=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

def push_zeros(arr):
    nonzero=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[nonzero],arr[i]=arr[i],arr[nonzero]
            nonzero+=1
            
    return arr