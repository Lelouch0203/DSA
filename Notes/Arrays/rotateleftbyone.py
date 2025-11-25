arr=[1,2,3,4,5,6,7]
# print(arr[4:]+arr[:4])
for i in range(3):
    temp=arr[-1]
    
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
        
    arr[0]=temp
print(arr)   
    