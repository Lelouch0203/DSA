nums=[1,-1,0]

k=0
cnt=0
mpp={}
mpp[0]=1
s=0
for i in range(len(nums)):
    s+=nums[i]
    rem=s-k
    cnt+=mpp.get(rem,0)
    mpp[s]=mpp.get(s,0)+1
    
    
print(cnt)