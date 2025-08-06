
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
        
def f(n):
    if n>0:
        f(n-1)
        print(n)
        f(n-1)
f(3)