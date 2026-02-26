def subseqsum(arr,i,k):
    if k < 0:
        return 0
    if k == 0:
        return 1
    if i == len(arr):
        return 1 if k == 0 else 0
    return subseqsum(arr,i+1,k-arr[i]) + subseqsum(arr,i+1,k)
print(subseqsum([4, 3, 9, 2],0,9))