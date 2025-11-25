def longestCommonPrefix(strs) -> str:
    mini=""
    minim=201
    for i in range(len(strs)):
        if len(strs[i])<(minim):
            mini=strs[i]
            minim=len(mini)
    print(mini)      

    count=0
    for i in range(len(mini)):
        for j in range(len(strs)):
            if strs[j][i]==mini[i]:
                print(strs[j][i],mini[i])
                continue
            else:
                return mini[:count]
        count+=1
        print(count)
    return (mini)
print(longestCommonPrefix(["flower","flow","flight"]))