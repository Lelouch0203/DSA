arr=[-2,-1,2,4,-2,4,-4] 
maxsum=0
s=0
# for i in range(len(arr)):
#     s=0
#     for j in range(i,len(arr)):
#         s+=arr[j]
#         maxsum=max(maxsum,s)
start=0
end=0
for i in range(len(arr)):
    s+=arr[i]
    
    if s>maxsum:
        maxsum=s
        end=i
        
    if s<0:
        s=0
        start=i
# print(sum(arr[3:-2]))
print(maxsum)
print(arr[start+1:end+1])

            