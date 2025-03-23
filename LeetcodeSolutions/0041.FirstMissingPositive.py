def firstMissingPositive(nums) -> int:
    num_set = set(nums) 
    smallest = 1
    while smallest in num_set: 
        smallest += 1
    return smallest

# my approach
def positive(arr):
    arr = sorted(set(arr))  
    if 1 not in arr:
        return 1
    for i in range(len(arr) - 1):
        if arr[i] > 0 and arr[i + 1] - arr[i] > 1:
            return arr[i] + 1
    return arr[-1] + 1 if arr[-1] > 0 else 1  