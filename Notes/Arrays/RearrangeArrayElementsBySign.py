nums=[3,1,-2,-5,2,-4,44,-34]
p=[]
n=[]
for i in nums:
    if i>0:
        p.append(i)
    else:
        n.append(i)
i=0
j=0
k=0
while i < len(nums):
    if i %2==0:
        nums[i]=p[j]
        i+=1
        j+=1
    else:
        nums[i]=n[k]
        i+=1
        k+=1
        
print(nums)
