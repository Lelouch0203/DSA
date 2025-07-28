def selectsort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min= j 
        arr[min],arr[i]=arr[i],arr[min]
    return arr
print(selectsort([13, 46, 24, 52, 20, 9]))