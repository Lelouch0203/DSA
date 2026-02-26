res = []
nums = [3,1,2]
# def subsetsum(i,s):
#     if i == len(nums):
#         res.append(s)
#         return
        
#     subsetsum(i+1,s)
#     subsetsum(i+1,s+nums[i])
def subsetsum(idx,s):
    
    res.append(s)
       
    for i in range(idx,len(nums)):
        subsetsum(i+1,s+nums[i])

subsetsum(0,0)
print(res)


    
    