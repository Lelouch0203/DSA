def bubblesort(arr):
    for i in range((len(arr)-1),0,-1):
        # didswap=False
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                didswap=True
        # if not didswap:
        #     break
        
    return arr
print(bubblesort([13, 46, 24, 52, 20, 9]))