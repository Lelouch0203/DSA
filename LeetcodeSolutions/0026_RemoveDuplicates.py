
def removeDuplicates(nums):
    i=0
    j=1
    while i!=len(nums) and j!=len(nums):
        if nums[i]==nums[j]:
            j+=1
        else:
            nums[i+1]=nums[j]
            j+=1
            i+=1
    
    return i+1 , nums
    

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))