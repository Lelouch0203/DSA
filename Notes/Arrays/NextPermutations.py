arr=[2,1,5,4,3,0,0]
def nextAss(arr):
    pvt=-1
    for i in range(len(arr)-2,-1,-1):
        if arr[i]<arr[i+1]:
            pvt=i
            break
    if pvt == -1:
        return reversed(arr)
    for i in range(len(arr)-1,pvt,-1):
        if arr[i]>arr[pvt]:
            arr[i],arr[pvt]=arr[pvt],arr[i]
            break
    n=(len(arr)-pvt)//2
    for i in range(pvt+1,n):
        arr[i],arr[(len(arr)-1)-(i+pvt+1)]=arr[(len(arr)-1)-(i+pvt+1)],arr[i]
    return arr
print(nextAss(arr))