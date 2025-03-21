def twoSum(arr,target):
    m={}
    for i,x in enumerate(arr):
        comp=target-x
        if comp not in m:
            m[x]=i
        else:
         return [m[comp],i]
print(twoSum(arr=[1,4,6,8],target=5))