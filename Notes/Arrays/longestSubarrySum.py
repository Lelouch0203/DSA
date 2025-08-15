req=9
# subarr=[]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         p=arr[i:j+1]
#         if sum(p) == req:
#             subarr.append([len(p),p])
# subarr.sort()
# print(subarr)
# print(subarr[-1][1])
arr=[-1,1,1]
def maxsub(arr):
    count=0
    suum=0
    maxi=0
    i=0
    while i<len(arr):
        suum+=arr[i]
        count+=1
        if suum ==2 or suum>2:
            # maxi=max(maxi,count)
            maxi = count if count > maxi else maxi
            count=0
            suum=0
        i+=1
        
    return maxi 
print(maxsub(arr))
            
                    
                
                
        

        
    
    