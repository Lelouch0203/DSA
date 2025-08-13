def singleNumber(nums):
        # m={}
        # for i in nums:
        #     m[i]=m.get(i,0)+1
            
        # arr=[]
        # for num,cnt in m.items():
        #     if cnt==1:
        #         return num
        x=0
        for i in nums:
            x=x^i
        return x
print(singleNumber([3,3,2,1,1]))