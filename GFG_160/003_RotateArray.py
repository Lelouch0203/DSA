def rotateArray(arr,d):
    if len(arr)==0:
        return arr
    d%=len(arr)
    parr=arr[d:]+arr[:d]
    for i in range(len(arr)):
                arr[i]=parr[i]
    return arr
arr=[1,2,3,45]
d=2
print(rotateArray(arr,2))
