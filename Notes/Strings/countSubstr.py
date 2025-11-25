def countss(s,k):
    letters={}
    ans=[]
    for i in range(len(s)):
        letters[s[i]]=letters.get(s[i],0)+1
        for j in range(i+1,len(s)):
            print(letters)
            if len(letters)==k:
                ans.append(s[i:j+1])
            if len(letters)>k:
                letters={}
                letters[s[i]]=letters.get(s[i],0)+1
    
    return ans
print(countss("pqpqs",2))