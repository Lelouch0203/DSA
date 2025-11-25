from collections import defaultdict
def isomo(s,t):
    # mf={}
    # mb={}
    # for i in range(len(s)):
    #     ch1=s[i]
    #     ch2=t[i]
    #     if (ch1 in mf.keys()):
    #         if mf[ch1]!=ch2:
    #             return False
    #     if  (ch2 in mb.keys()):
    #         if mb[ch2]!=ch1:
    #             return False
    #     mf[ch1]=ch2
    #     mb[ch2]=ch1
 
    # return True
    mapping = defaultdict(str)
    mapped = set()
    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]]==t[i]:
                continue
            else:
                return False
        else:
            if t[i] not in mapped:
                mapping[s[i]]=t[i]
                mapped.add(t[i])
            else:
                return False
    return True
    
    
print(isomo('paper','title'))