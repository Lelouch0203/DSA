def largeestnum(arr):
    # return max(arr)
    #for nlogn sort and return [-1]
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest
print(largeestnum([2,5,1,3,0]))
