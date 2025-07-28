import math
arr = [1,2,3,4]

prd = math.prod(arr)
for i in range(len(arr)):
    arr[i]=prd/arr[i]
    # i=prd/i
arr = list(map(int,arr))
print(arr)
