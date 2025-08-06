from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list)
    
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))