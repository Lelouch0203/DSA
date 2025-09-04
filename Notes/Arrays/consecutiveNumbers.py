import time

start_time = time.time()
nums=[100,4,200,1,3,2]
def longAss(nums):
    maxi=0
    if len(nums)==0:
        return 0
    numset=sorted(list(set(nums)))
    
    
    
    # for num in numset:
    #     if num-1 not in numset:
    #         lleenn=1
    #         while num+lleenn in numset:
    #             lleenn+=1
    #         maxi=max(lleenn,maxi)
    
    
    
    
    cnt=1
    for i in range(len(numset)-1):
        if numset[i+1]-numset[i]==1:
            cnt+=1
        else:
            cnt=1
        maxi=max(cnt,maxi)
        
        
        
    
    return maxi
print(longAss(nums))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")
