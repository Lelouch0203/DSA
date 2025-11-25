def maxnest(s):
    cnt=0
    maxi=0
    for chr in s:
        if chr == '(':
            cnt+=1
        if chr==")":
            cnt-=1
        maxi=max(cnt,maxi)
    return maxi
print(maxnest("(1)+((2))+(((3)))"))