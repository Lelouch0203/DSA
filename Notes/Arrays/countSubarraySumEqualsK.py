
from collections import defaultdict
nums=[1,-1,0]

k=0

# for i in range(len(nums)):
#     s=nums[i]
#     for j in range(i+1,len(nums)):
#         s+=nums[j]
#         # print(s)
#         if s==k:
#             count+=1
#             break
# cnt=0        
# presum=0
# mpp=defaultdict(int)
# mpp[0]=1
# for i in range(len(nums)):
#     presum+=nums[i]
#     remove = presum -k 
#     cnt+=mpp[remove]
#     mpp[presum]+=1
cnt=0
mpp={}
mpp[0]=1
s=0
for i in range(len(nums)):
    s+=nums[i]
    rem=s-k
    cnt+=mpp.get(rem,0)
    mpp[s]=mpp.get(s,0)+1
    
# print(mpp)
        

        


print(cnt)