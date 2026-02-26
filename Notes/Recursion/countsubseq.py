def count(arr,i,k):
    if k < 0 :
        return 0
    if k == 0:
        return 1
    if i == len(arr):
        if k == 0:
            return 1
        return 0
    return count(arr,i+1,k-arr[i]) + count(arr,i+1,k)
    
print(count([4, 2, 10, 5, 1, 3],0,5))