
def removeOuterParentheses(s):
    ans=""
    cnt=0
    for ch in s:
        print(cnt)
        if ch=='(':
            if cnt>0:
                ans+=ch
            cnt+=1
        else:
            cnt-=1
            if cnt>0:
                ans+=ch
    return ans
print(removeOuterParentheses("(()())(())"))