    

def partition(arr, low, high):
    pvt = low
    i = low + 1
    j = high
    while True:
        while i <= high and arr[i] <= arr[pvt]:
            i += 1
        while arr[j] > arr[pvt]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[j], arr[pvt] = arr[pvt], arr[j]
    return j



    
    
def quick(arr,low,high):
    if low<high:
        j=partition(arr,low,high)
        quick(arr,low,j-1)
        quick(arr,j+1,high)
    return arr

print(quick([20,10,40,15,6,30],0,5))