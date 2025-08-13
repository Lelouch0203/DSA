nums=[1,1,1,1,0,1,0,1,1,1,1,1,1]
count,maxi=0,0
# for i in nums:
#     if i == 1:
#         count+=1
#         maxi=max(maxi,count)
#     else:
#         count=0
        
for i in nums:
    if i==1:
        count+=1
    else:
        maxi=count if maxi<count else maxi
        count=0
if count>0 :
    print(count if count>maxi else print (maxi))
else:
    print(maxi)


    
