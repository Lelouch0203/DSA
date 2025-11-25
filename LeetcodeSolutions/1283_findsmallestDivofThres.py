import math
def smallestDivisor(self, nums, threshold: int) -> int:

        def divcheck(nums,div):
            Sum=0
            for num in nums:
                Sum+=math.ceil(num/div)
            return Sum
        if len(nums)>threshold:
         return -1
        l=1
        r=max(nums)
        
        while l<=r:
            mid=(l+r)//2
            if divcheck(nums,mid)<=threshold:
                r=mid-1
            else:
                l=mid+1
        return l
    
print(smallestDivisor(0,[1,2,5,9],6))