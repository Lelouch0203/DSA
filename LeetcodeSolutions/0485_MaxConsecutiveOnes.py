nums=[1,1,1,0,1,0,1,1,1,1]
def maxones(nums):
    count=0
    maxi=0
    for i in nums:
        if i==1:
            count+=1
        else:
            maxi=count if maxi<count else maxi
            count=0
    if count>0:
        return count if count>maxi else maxi
    else:
        return maxi
    
print(maxones(nums))