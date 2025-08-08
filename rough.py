
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