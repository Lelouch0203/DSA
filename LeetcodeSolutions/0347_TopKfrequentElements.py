import heapq as hq
nums=[1,1,1,2,2,3]
k=2
count={}
for i in nums:
    count[i]=count.get(i,0)+1
    
# heap--------------------------------------------------------------------------------------------
# heap=[]
# for num,cnt in count.items():
#     hq.heappush(heap,(cnt,num))
#     if len(heap)>k:
#         hq.heappop(heap)
# res=[]
# for i in range(k):
#     res.append(hq.heappop(heap)[1])
# print(res)


# arr=[]
# for num,cnt in count.items():
#     arr.append([cnt,num])
# arr.sort()
# res=[]
# while len(res)<k:
#     res.append(arr.pop()[1])

# print(res)


# bucketsort----------------------------------------------------------------------------------------
freq=[[] for i in range(len(nums)+1)]
for num,cnt in count.items():
    freq[cnt].append(num)
res=[]
for i in range(len(freq)-1,0,-1):
    for num in freq[i]:
        res.append(num)
        if len(res)==k:
            print(res)
            break

