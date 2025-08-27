import heapq
from collections import defaultdict

# def groupAnagrams(strs):
#     res = defaultdict(list)
#     for s in strs:
#         sortedS = ''.join(sorted(s))
#         res[sortedS].append(s)
#     return list(res.values())
# def groupAnagrams(strs):
#     res = defaultdict(list)
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         res[tuple(count)].append(s)
#     return list(res.values())
# def gn(strs):
#     res = defaultdict(list)
#     for s in strs:
#         sortedS = ''.join(sorted(s))
#         res[sortedS].append(s)
#     return list(res.values())
# def gn2(strs):
#     res= defaultdict(list)
#     for s in strs:
#         count=[0]*26
#         for c in s:
#             count[ord(c)-ord('a')]+=1
#         res[tuple(count)].append(s)
#     return list(res.values())

# print(gn2(["act","pots","tops","cat","stop","hat"]))
        
# nums=[3,4,5,1,2]
# # if nums == sorted(nums):
# #     print("t")
# for i in range(len(nums)-1):
#     if nums[i]>nums[i+1]:
#         nums=nums[i+1:]+nums[:i+1]
#         print(nums)
#         print(nums==sorted(nums))
# nums=[1,1,1,1,2,2,3]
# k=2
# count = {}
# for num in nums:
#     count[num] = 1 + count.get(num, 0)

# heap = []
# for num in count.keys():
#     heapq.heappush(heap, (count[num], num))
    
#     if len(heap) > k:
#         heapq.heappop(heap)

# res = []
# for i in range(k):
#     res.append(heapq.heappop(heap)[1])
# # return res
# print(res) 
# freq = [[] for i in range(len(nums))]

# # for num in nums:
# #     count[num] = 1 + count.get(num, 0)
# for num, cnt in count.items():
#     freq[cnt-1].append(num)
# print(freq)

# res = []
# for i in range(len(freq) - 1, 0, -1):
#     for num in freq[i]:
#         res.append(num)
#         if len(res) == k:
#             print(res)
#             break




# Input=["neet","code","love","you"]
# s=''
# for i in Input:
#     s+=str(len(i))+i
# print(s)
# arr=[]
# i=0
# while i<len(s):
#     j=i+1
#     for j in range(int(i)):
        
        
    
    

# nums=[-1,0,1,2,3]
# whole=1
# for i in nums:
#     whole*=i
# for i in range(len(nums)):
#     if nums[i]==0:
#         nums[i]=-6
#         continue
#     nums[i]=whole//nums[i]
# print(nums)


# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         curr=arr[j]-arr[i]
#         maxi=max(maxi,curr)
#         print(maxi)
#         # print('-')
# print(maxi)


# arr=[7,1,5,3,6,4]
# maxpro=0
# minP=float('inf')
# for i in range(len(arr)):
#     minP=min(arr[i],minP)
#     print(arr[i],minP,end=",")
#     maxpro=max(maxpro,arr[i]-minP)
#     print(maxpro)
#     print("____________________________________")
# print(maxpro)
    
# strs='23232'
# strs_list = list(strs)
# strs_list[0] = '4'
# strs = ''.join(strs_list)
    
# def sumofdig(num):
#     summ=0
#     while num>0:
#         summ+=num%10
#         num//=10
#     return summ
# # print(sumofdig(23))
# nums=list(map(int,input().split()))
# # nums=[]
# count={}
# for num in nums:
#     i=sumofdig(num)   
#     count[i]=count.get(i,0)+1
# print(count)
# ans=0
# for sm,nos in count.items():

#     if nos>=2:
#         ans+=(nos*(nos-1))//2
# print(ans)
        
# arr=[-1,1,3,3,15,6,3,-3,3,-5,-7]
# posi=0
# for i in range(len(arr)):
#     if arr[i]<0:
#         arr[i],arr[posi]=arr[posi],arr[i]
#         posi+=1
# print(arr)


arr=[1,2,3,4,5]
for i in range(len(arr)//2):
    arr[i],arr[(len(arr)-1)-i]=arr[(len(arr)-1)-i],arr[i]
print(arr)