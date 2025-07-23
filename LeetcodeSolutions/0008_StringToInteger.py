def myAtoi(self, s: str) -> int:
    s=s.strip()
    if not s:
        return 0
        
    ans= "-" if s[0]=="-" else ""

    nums="1234567890"
    start=0
    if s[0]=="-" or s[0]=="+":
        start+=1 
    for i in range(start,len(s)):
        if s[i] in nums:
            ans+=s[i]
        else:
            break

    result = int(ans) if ans not in ["", "-"] else 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    return result
print(myAtoi('',"five"))