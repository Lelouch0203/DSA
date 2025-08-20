arr=[-2,1,-3,4,-1,2,1,-5,4] 
maxsum=0
s=0
# for i in range(len(arr)):
#     s=0
#     for j in range(i,len(arr)):
#         s+=arr[j]
#         maxsum=max(maxsum,s)
for i in range(len(arr)):
    s+=arr[i]
    if s>maxsum:
        maxsum=s
    if s<0:
        s=0
# print(sum(arr[3:-2]))
print(maxsum)

            