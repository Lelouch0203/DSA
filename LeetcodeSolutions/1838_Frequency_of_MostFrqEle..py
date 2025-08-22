arr=[3,4,5,12,19,22,44,150]
k=32
arr.sort()
left=0
maxlenofwin=0
sumofwin=0
for right in range(len(arr)):
    sumofwin+=arr[right]
    target=arr[right]
    


    while target*(right-left+1)-sumofwin>k:

        sumofwin-=arr[left]
        left+=1
    maxlenofwin=max(maxlenofwin,right-left+1)
print(maxlenofwin)      