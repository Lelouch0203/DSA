
def anagram(s,t):
    ok=[0]*26
    for i in range(len(s)):
        ok[(ord(s[i])-ord('a'))]+=1
        ok[(ord(t[i])-ord('a'))]-=1
    for i in range(len(ok)):
        if ok[i]!=0:
            return False
    return True
        
        
