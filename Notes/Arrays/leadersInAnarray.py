arr=[10, 22, 12, 3, 0, 6]
ans=[]
# for i in range(len(arr)):
#     leader=True
#     for j in range(i+1,len(arr)):
#         if arr[i]<arr[j]:
#             leader = False
#             break 
#     if leader:
#         ans.append(arr[i])
maxi=0
for i in range(len(arr)-1,-1,-1):
    if arr[i]>maxi:
        ans.append(arr[i])
        maxi=arr[i]
    
    

print(ans)
            
            
            