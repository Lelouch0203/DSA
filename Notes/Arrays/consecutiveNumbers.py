nums=[100,4,200,1,3,2]
maxi=0
if len(nums)==0:
    print("0") 
numset=sorted(list(set(nums)))
print(numset)
# for num in numset:
#     if num-1 not in numset:
#         length =1
#         while num+length in numset:
#             length+=1
#         maxi=max(length,maxi)
cnt=1
for i in range(len(numset)-1):
    if numset[i+1]-numset[i]==1:
        cnt+=1
    else:
        cnt=1
    maxi=max(cnt,maxi)
        
    
        

print(maxi)