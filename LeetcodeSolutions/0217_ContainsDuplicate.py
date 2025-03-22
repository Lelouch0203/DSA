def containsDuplicate(nums):
    return len(nums) != len(set(nums))
nums=[1,2,3,4,2,2,556,7,8,4,7,4,32,36,7,78454,3,2342,]
print(containsDuplicate(nums))