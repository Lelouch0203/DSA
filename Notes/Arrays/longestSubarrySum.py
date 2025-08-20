
# for i in range(n):
#     for j in range(i,n):
#         sm=0
#         for o in range(i,j+1):
#             sm+=arr[o]
#         if sm==k:
#             length=max(length,j-i+1)
# print(length)

# for i in range(n):
#     s=0
#     for j in range(i,n):
#         s+=arr[j]
#         if s==k:
#             length= max(length,j-i+1)
# print(length)

arr = [2,3,5,1,9]
k=9
n=len(arr)

preSum={}
s=0
maxlen=0
for i in range(n):
    s+=arr[i]
    if s==k:
        maxlen=i+1
    rem=s-k
    if rem in preSum:
        length=i-preSum[rem]
        maxlen=max(maxlen,length)
    if s not in preSum:
        preSum[s]=i
print(maxlen)
print(preSum)


