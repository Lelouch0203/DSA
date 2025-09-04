def longestConsecutive(nums):
    maxi=0
    if len(nums)==0:
        return 0 
    numset=set(nums)
    for num in numset:
        if num-1 not in numset:
            length=1
            while num+length in numset:
                length +=1
            maxi=max(maxi,length)

    return maxi